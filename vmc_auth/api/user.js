const express = require("express");
const User = require("../models/user");
const router = express.Router();

const bcrypt = require("bcrypt");

// SignUp

router.post("/signup", (req, res) => {
  let { name, email, password, mobile, publicAddress } = req.body;
  name = name.trim();
  email = email.trim();
  password = password.trim();
  mobile = mobile.trim();
  publicAddress = publicAddress.trim();

  if (
    name === "" ||
    email === "" ||
    password === "" ||
    mobile === "" ||
    publicAddress === ""
  ) {
    res.json({
      status: "FAILED",
      message: "Empty input field(s)!",
    });
  } else if (!/^0x[a-fA-F0-9]{40}$/.test(publicAddress)) {
    res.json({
      status: "FAILED",
      message: "Please enter a valid public address!",
    });
  } else {
    User.find({ email })
      .then((response) => {
        if (response.length) {
          res.json({
            status: "FAILED",
            message: "User already exists! Please use another email id...",
          });
        } else {
          const saltRounds = 10;
          bcrypt
            .hash(password, saltRounds)
            .then((hashedPassword) => {
              const newUser = new User({
                name,
                email,
                password: hashedPassword,
                mobile,
                publicAddress,
              });
              newUser
                .save()
                .then((response) => {
                  res.json({
                    status: "SUCCESS",
                    message: "User registered successfully!",
                    data: response,
                  });
                })
                .catch((err) => {
                  res.json({
                    status: "FAILED",
                    message:
                      "An unexpected error occurred while registering! Please check your internet connection and try again...",
                  });
                });
            })
            .catch((err) => {
              res.json({
                status: "FAILED",
                message:
                  "An unexpected error occurred while registering! Please check your internet connection and try again...",
              });
            });
        }
      })
      .catch((err) => {
        res.json({
          status: "FAILED",
          message:
            "An unexpected error occurred while registering! Please check your internet connection and try again...",
        });
      });
  }
});

// Login

router.post("/login", (req, res) => {
  let { email, password, publicAddress } = req.body;
  email = email.trim();
  password = password.trim();
  publicAddress = publicAddress.trim();

  if (email === "" || password === "" || publicAddress === "") {
    res.json({
      status: "FAILED",
      message: "Inadequate credentials! Please fill all the fields...",
    });
  } else if (!/^0x[a-fA-F0-9]{40}$/.test(publicAddress)) {
    res.json({
      status: "FAILED",
      message: "Please enter a valid public address!",
    });
  } else {
    User.find({ email, publicAddress })
      .then((response) => {
        if (response) {
          const hashedPassword = response[0].password;
          bcrypt
            .compare(password, hashedPassword)
            .then((response) => {
              if (response) {
                res.json({
                  status: "SUCCESS",
                  message: "User logged in successfully!",
                });
              } else {
                res.json({
                  status: "FAILED",
                  message: "Please enter the correct password and try again!",
                });
              }
            })
            .catch((err) => {
              res.json({
                status: "FAILED",
                message:
                  "An unexpected error occurred while logging in! Please check your internet connection and try again...",
              });
            });
        } else {
          res.json({
            status: "FAILED",
            message:
              "Invalid credentials entered! Please verify your credentials and try again...",
          });
        }
      })
      .catch((err) => {
        res.json({
          status: "FAILED",
          message:
            "Invalid credentials entered! Please verify your credentials and try again...",
        });
      });
  }
});

module.exports = router;
