require("dotenv").config();
require("./config/db");
const userRouter = require("./api/user");
var cors = require("cors");

const app = require("express")();
app.use(cors());

const port = process.env.PORT;

const bodyParser = require("express").json();
app.use(bodyParser);

app.use("/user", userRouter);

app.listen(port, () => {
  console.log(`Server running on port: ${port}`);
});
