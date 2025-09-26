YOUTUBE --> LINK -->
RESTful CRUD API with Node.js, Express, and PostgreSQL || Schema Creation using Sequelize || PART-1

1. create a Desktop folder
2. open vs code
3. first time install PostgreSQL (and pgAdmin)
4. Create a folder name server
5. open terminal
6. cd server
7. npm init -y
8. npm i nodemon express
9. check dependencies (package.json)
10. create a file index.js
11. package.json changes --> "type": "module",
12. package.json changes --> scripts --> "start": "nodemon index.js",
13. after the code run --> npm run start

14. npm install --save sequelize
15. npm install --save pg pg-hstore
16. create a file postgres/postgres.js
17. copy code from Sequelize docs for connecting database
18. in postgres file set dialect: 'postgres'

Example postgres/postgres.js:
```js
import { Sequelize } from "sequelize";

const sequelize = new Sequelize("your_database", "your_db_user", "your_password", {
  host: "localhost",
  dialect: "postgres",
});

export default sequelize;

export const Connection = async () => {
  try {
    await sequelize.authenticate();
    console.log("✅ Connection has been established successfully.");
    await sequelize.sync();
    console.log("✅ Database synced");
  } catch (error) {
    console.error("❌ Unable to connect to the database:", error);
  }
};


open pgAdmin and make sure DB/user/password match the code above


---

YOUTUBE -->  
**RESTful CRUD API with Node.js, Express, and PostgreSQL || Schema Creation using Sequelize || PART-2**



create 3 folders inside server:
server/postgres
server/view
server/controller
server/model

in model folder create file --> userSchema.js

create userSchema code (lines ~1 to 26)


`server/model/userSchema.js` (lines ~1–26)
```js
import { DataTypes } from "sequelize";

export const createUserModel = (sequelize) => {
  return sequelize.define("User", {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    designation: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    empid: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
  });
};


YOUTUBE -->
RESTful CRUD API with Node.js, Express, and PostgreSQL || GET-Method || PART-3

1. create a folder view --> create file routes.js
2. check all files are present (index.js, postgres/postgres.js, model/userSchema.js, controller/userController.js, view/routes.js)
3. create a file controller --> userController.js
4. Implement GET API: check API for GET method


Example server/view/routes.js:

import express from "express";
import { getAllEmp } from "../controller/userController.js";

const router = express.Router();

router.get("/users", getAllEmp);

export default router;


Example server/controller/userController.js (GET):

import { UserModel } from "../postgres/postgres.js";

export const getAllEmp = async (req, res) => {
  try {
    const users = await UserModel.findAll();
    if (!users.length) return res.status(200).json({ error: "user not Found" });
    return res.status(200).json(users);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "internal server error" });
  }
};


YOUTUBE -->
RESTful CRUD API with Node.js, Express, and PostgreSQL || POST-Method || PART-4

1. add code for POST in routes.js and controller
2. npm i cors
3. enable CORS in index.js
4. testing API using Thunder Client / Postman


Example POST route & handler:

// routes.js
router.post("/add", addEmp);

// userController.js
export const addEmp = async (req, res) => {
  try {
    const { empid } = req.body;
    const existing = await UserModel.findOne({ where: { empid } });
    if (!existing) {
      const created = await UserModel.create(req.body);
      return res.status(201).json({ message: "emp added successfully", data: created });
    }
    return res.status(200).json({ message: "already found" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};


YOUTUBE -->
RESTful CRUD API with Node.js, Express, and PostgreSQL || PUT Method || PART-5

1. add PUT route in routes.js (e.g., PUT /update/:empid)
2. implement updateEmp in controller
3. test API for update via Thunder Client


Example update:

// routes.js
router.put("/update/:empid", updateEmp);

// controller
export const updateEmp = async (req, res) => {
  try {
    const { empid } = req.params;
    const [updatedRows] = await UserModel.update(req.body, { where: { empid } });
    if (updatedRows === 0) return res.status(404).json({ message: "emp not found" });
    return res.status(200).json({ message: "updated successfully" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};


YOUTUBE -->
RESTful CRUD API with Node.js, Express, and PostgreSQL || DELETE Method || PART-6

1. add DELETE route in routes.js (e.g., DELETE /delete/:empid)
2. implement deleteEmp in controller
3. test API for delete
4. check all code and finalize


Example delete:

// routes.js
router.delete("/delete/:empid", deleteEmp);

// controller
export const deleteEmp = async (req, res) => {
  try {
    const { empid } = req.params;
    const deleted = await UserModel.destroy({ where: { empid } });
    if (!deleted) return res.status(404).json({ message: "emp not found" });
    return res.status(200).json({ message: "deleted successfully" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};


Final Notes / Reminders (do not change this document — only follow steps above):

- Always include .js extension in imports when using "type": "module":
  import router from "./view/routes.js";
  import { Connection, UserModel } from "./postgres/postgres.js";

- Install required packages in your project folder:
  npm install express nodemon sequelize pg pg-hstore cors

- Check postgres credentials in postgres/postgres.js (use your DB name, username, password).

- Start server:
  npm run start

- Test endpoints in Thunder Client:
  GET  http://localhost:8000/users
  POST http://localhost:8000/add  (body JSON)
  PUT  http://localhost:8000/update/:empid
  DELETE http://localhost:8000/delete/:empid


Agar chaho to main ab exactly is document ko ek text/markdown file bana ke (ready to copy) de doon — ya phir main aapke current files ke liye ready-to-paste exact contents provide kar doon (index.js, postgres/postgres.js, model/userSchema.js, view/routes.js, controller/userController.js). Kaunsa chahoge?

You said:
yes
ChatGPT said:

Thik hai 👍 — ab main aapko ready-to-paste final folder/files structure + code bana kar de raha hoon. Isse aap directly apne server folder mai paste karke run kar sakte ho.

📂 Project Structure
server/
│── index.js
│
├── postgres/
│   └── postgres.js
│
├── model/
│   └── userSchema.js
│
├── controller/
│   └── userController.js
│
└── view/
    └── routes.js

1️⃣ index.js
import express from "express";
import cors from "cors";
import router from "./view/routes.js";
import { Connection } from "./postgres/postgres.js";

const app = express();
const PORT = 8000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use("/", router);

// Start server
app.listen(PORT, async () => {
  console.log(`✅ Server is running on port ${PORT}`);
  await Connection();
});

2️⃣ postgres/postgres.js
import { Sequelize } from "sequelize";
import { createUserModel } from "../model/userSchema.js";

const sequelize = new Sequelize("your_database", "your_user", "your_password", {
  host: "localhost",
  dialect: "postgres",
});

let UserModel = null;

const Connection = async () => {
  try {
    await sequelize.authenticate();
    console.log("✅ Connection has been established successfully.");
    UserModel = createUserModel(sequelize);
    await sequelize.sync();
    console.log("✅ Database synced");
  } catch (error) {
    console.error("❌ Unable to connect to the database:", error);
  }
};

export { Connection, UserModel };


👉 Replace:

"your_database" → aapke DB ka naam (pgAdmin mai banaya hai)

"your_user" → Postgres username (default: postgres)

"your_password" → Postgres password (jo setup ke time set kiya tha)

3️⃣ model/userSchema.js
import { DataTypes } from "sequelize";

export const createUserModel = (sequelize) => {
  return sequelize.define("User", {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    designation: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    empid: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
  });
};

4️⃣ controller/userController.js
import { UserModel } from "../postgres/postgres.js";

// GET all users
export const getAllEmp = async (req, res) => {
  try {
    const users = await UserModel.findAll();
    if (!users.length) return res.status(404).json({ error: "user not Found" });
    return res.status(200).json(users);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "internal server error" });
  }
};

// POST add user
export const addEmp = async (req, res) => {
  try {
    const { empid } = req.body;
    const existing = await UserModel.findOne({ where: { empid } });
    if (!existing) {
      const created = await UserModel.create(req.body);
      return res.status(201).json({ message: "emp added successfully", data: created });
    }
    return res.status(400).json({ message: "emp already exists" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};

// PUT update user
export const updateEmp = async (req, res) => {
  try {
    const { empid } = req.params;
    const [updatedRows] = await UserModel.update(req.body, { where: { empid } });
    if (updatedRows === 0) return res.status(404).json({ message: "emp not found" });
    return res.status(200).json({ message: "updated successfully" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};

// DELETE user
export const deleteEmp = async (req, res) => {
  try {
    const { empid } = req.params;
    const deleted = await UserModel.destroy({ where: { empid } });
    if (!deleted) return res.status(404).json({ message: "emp not found" });
    return res.status(200).json({ message: "deleted successfully" });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "internal server error" });
  }
};

5️⃣ view/routes.js
import express from "express";
import { getAllEmp, addEmp, updateEmp, deleteEmp } from "../controller/userController.js";

const router = express.Router();

// Routes
router.get("/users", getAllEmp);
router.post("/add", addEmp);
router.put("/update/:empid", updateEmp);
router.delete("/delete/:empid", deleteEmp);

export default router;

6️⃣ Install dependencies
npm install express nodemon sequelize pg pg-hstore cors

7️⃣ Start Server
npm run start

8️⃣ Test in Thunder Client / Postman

GET → http://localhost:8000/users

POST → http://localhost:8000/add

{
  "name": "Ali",
  "email": "ali@test.com",
  "designation": "Manager",
  "empid": "EMP101"
}


PUT → http://localhost:8000/update/EMP101

DELETE → http://localhost:8000/delete/EMP101