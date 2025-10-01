# # Starting Process for backend-db


# // YOUTUBE --> LINK -->
# // RESTful CRUD API with Node.js, Express, and PostgreSQL|| Schema Creation using Sequelize || PART-1

# // create a  Desktop folder
# // open vs code
# // first time install PostgresSQL
# // Create a folder name server
# // open terminal
# // cd server
# // npm init
# // npm i nodemon express
# // npm install --save sequelize
# // npm install --save pg pg-hstore 
# // check depencies
# // creata a file index.js
# // Depencies changes --> "type": "module",
# // Depencies changes -->  Script --> "start": "nodemon index.js",
# // after The code run --> npm run satrt

# // create a folder postgres and file postgres.js
# // copy code Sequelize Documents for connecting DataBase
# // postgres file mai say --> select database for dialect:  'postgres'

# // import { Sequelize } from 'sequelize';
# // open pgAdmin
# // set this --> const sequelize = new Sequelize('database--> postgres', 'username' --> roort , 'password--> root'




# // YOUTUBE -->
# // RESTful CRUD API with Node.js, Express, and PostgreSQL|| Schema Creation using Sequelize || PART-2

# // create a 3 folder 
# // postgres 1 folder mai --> view 
# // server 2 folder mai --> controller --> model 
# // model k folder mai file create karni hai --> userSchema.js
# // create a userSchema code line # 1 To 26


# // YOUTUBE -->
# // RESTful CRUD API with Node.js, Express, and PostgreSQL || GET-Method || PART-3

# // creata a file folder-name view --> route.js
# // all files checking 
# // create a file controller --> userController.js
# // CHECK Api for get method

# // YOUTUBE -->
# // RESTful CRUD API with Node.js, Express, and PostgreSQL|| POST-Method || PART-4

# // codes
# // npm i cors
# // testing Api for thunder client
# // chaeck api for post


# // YOUTUBE  -->
# // RESTful CRUD API with Node.js, Express, and PostgreSQL|| PUT Method || PART-5

# // check api for updated


# // Youtube ==>
# // RESTful CRUD API with Node.js, Express, and PostgreSQL|| DELETE Method || PART-6

# // check api for delete
# // check all code
# // Final code


# // connect with frontend
# // http://localhost:5000/routes name
# // 









# # fILE STRUCTURE for backend-db userModel
# folder --> server
# folder --> controller
#   file --> user-controller.js
# folder --> model
#   file --> user-model.js
# folder --> postgres
#   file --> postgres.js
# folder --> view
#   file --> User-routes.js
# index.js 

# # File Structure for backend-db todoModel
# folder --> server
# folder --> controller
#   file --> todo-controller.js
# folder --> model
#   file --> todo-model.js
# folder --> postgres
#   file --> postgres.js
# folder --> view
#     file --> Todo-routes.js
# index.js


# Controller 
# user-controller.js
    # import { UserModel } from "../postgres/postgres.js";

    # export const getAllEmp = async (req, res) => {
    # try {
    #     const users = await UserModel.findAll();
    #     if (users.length == 0) {
    #     return res.status(200).json({ error: "user not Found" });
    #     }

    #     return res.status(200).json(users);
    # } catch (error) {
    #     console.log(error);

    #     return res.status(500).json({ error: "internal server error" });
    # }
    # };

    # export const addEmp = async (req, res) => {
    # const { name, email, designation, empid } = req.body;
    # try {
    #     const emp = await UserModel.findOne({ where: { empid: empid } });
    #     if (emp == null) {
    #     await UserModel.create(req.body);
    #     return res.status(201).json({ message: "emp added successfully" });
    #     }

    #     return res.status(200).json({ message: "already found" });
    # } catch (e) {
    #     console.log(e);
    #     return res.status(500).json({ error: "internal server error" });
    # }
    # };

    # export const updateEmp = async (req, res) => {
    # const { empid } = req.params;
    # try {
    #     const emp = await UserModel.update(req.body, { where: { empid } });

    #     if (emp[0] == 0) return res.status(200).json({ message: "emp not found" });

    #     return res.status(200).json({ message: "updated successfully" });
    # } catch (e) {
    #     console.log(e);
    #     return res.status(500).json({ error: "internal server error" });
    # }
    # };

    # export const deleteEmp = async (req, res) => {
    # const { empid } = req.params;
    # try {
    #     const emp = await UserModel.destroy({ where: { empid } });
    #     if (emp === 0) return res.status(404).json({ message: "emp not found" });
    #     return res.status(200).json({ message: "deleted successfully" });
    # } catch (e) {
    #     console.log(e);
    #     return res.status(500).json({ error: "internal server error" });
    # }
    # };

# todo-controller.js
# import { TodoModel } from "../postgres/postgres.js";

# export const getAllTodo = async (req, res) => {
#     try {
#         const todoList = await TodoModel.findAll();
#         if (todoList.length == 0) {
#             return res.status(200).json({ error: "Todo list not Found" });
#         }

#         return res.status(200).json(todoList);
#     } catch (error) {
#         console.log(error);

#         return res.status(500).json({ error: "internal server error" });
#     }
# };

# export const addTodo = async (req, res) => {
#     console.log("this is the req body", req.body);
#     const { name } = req.body;
#     console.log("this is the name", name);
#     try {

#         await TodoModel.create({ name });
#         return res.status(201).json({ message: "todo added successfully" });

#     } catch (e) {
#         console.log(e);
#         return res.status(500).json({ error: "internal server error" });
#     }
# };

# // export const updateTodo = async (req, res) => {
# // const { todoId } = req.params;
# // try {
# //     const todo = await TodoModel.update(req.body, { where: { todoId } });

# //     if (todo[0] == 0) return res.status(200).json({ message: "todo not found" });

# //     return res.status(200).json({ message: "updated successfully" });
# // } catch (e) {
# //     console.log(e);
# //     return res.status(500).json({ error: "internal server error" });
# // }
# // };

# // export const deleteTodo = async (req, res) => {
# // const { todoId } = req.params;
# // try {
# //     const todo = await TodoModel.destroy({ where: { todoId } });
# //     if (todo === 0) return res.status(404).json({ message: "emp not found" });
# //     return res.status(200).json({ message: "deleted successfully" });
# // } catch (e) {
# //     console.log(e);
# //     return res.status(500).json({ error: "internal server error" });
# // }
# // };

# export const updateTodo = async (req, res) => {
#     const { id } = req.params;

#     try {
#         const [updatedCount, updatedRows] = await TodoModel.update(
#             req.body,
#             { where: { id }, returning: true } // returning works in Postgres
#         );

#         if (updatedCount === 0) {
#             return res.status(404).json({ message: "todo not found" });
#         }

#         return res.status(200).json({
#             message: "updated successfully",
#             todo: updatedRows[0]   // send back the updated todo
#         });
#     } catch (e) {
#         console.error(e);
#         return res.status(500).json({ error: "internal server error" });
#     }
# };

# export const deleteTodo = async (req, res) => {
#     const { id } = req.params;
#     try {
#         const todo = await TodoModel.destroy({ where: { id } });
#         if (todo === 0) return res.status(404).json({ message: "todo not found" });
#         return res.status(200).json({ message: "deleted successfully" });
#     } catch (e) {
#         console.log(e);
#         return res.status(500).json({ error: "internal server error" });
#     }
# };


# Model
# user-model.js
#     import { DataTypes } from "sequelize";

# export const createUserModel = async (sequelize) => {
#   const User = sequelize.define("User", {
#     name: {
#       type: DataTypes.STRING,
#       allowNull: false,
#     },
#     email: {
#       type: DataTypes.STRING,
#       allowNull: false,
#       isLowercase: true,
#       unique: true,
#     },
#     designation: {
#       type: DataTypes.STRING,
#       allowNull: false,
#     },
#     empid: {
#       type: DataTypes.STRING,
#       allowNull: false,
#       unique: true,
#     },
#   });
#   return User;
# };


# todo-model.js

#   import { DataTypes } from "sequelize";

#   export const createTodoModel = async (sequelize) => {
#     const Todo = sequelize.define("Todo", {
#       name: {
#         type: DataTypes.STRING,
#         allowNull: false,
#       }
#     });
#     return Todo;
#   };


# Postgres
# postgres.js
# // // Option 3: Passing parameters separately (other dialects)
# // Sequelize Documentation

# import { Sequelize } from "sequelize";
# import { createUserModel } from "../model/userSchema.js";
# import { createTodoModel } from "../model/todoSchema.js";


# const sequelize = new Sequelize("postgres", "postgres", "12345", {
#   host: "localhost",
#   dialect: "postgres",
# });

# let UserModel = null;
# let TodoModel = null
# const connection = async () => {
#   try {
#     await sequelize.authenticate();
#     console.log(" Connection has been established successfully.");

#     UserModel = await createUserModel(sequelize);
#     TodoModel = await createTodoModel(sequelize);
#     await sequelize.sync();
#     console.log("Database synced");
#   } catch (error) {
#     console.error(" Unable to connect to the database:", error);
#   }
# };

# export { connection, UserModel, TodoModel };



# View
# User-routes.js
# import express from "express";
# import {
#   getAllEmp,
#   addEmp,
#   updateEmp,
#   deleteEmp,
# } from "../controller/userController.js";

# const router = express.Router();

# router.get("/getAll", getAllEmp);
# router.post("/addEmp", addEmp);
# router.put("/emp/:empid", updateEmp);
# router.delete("/emp/:empid", deleteEmp);

# export default router;

# Todo-routes.js

# import express from "express";
# import {
#   addTodo,deleteTodo,getAllTodo,updateTodo
# } from "../controller/todoController.js";

# const router = express.Router();

# router.get("/getAll", getAllTodo);
# router.post("/addTodo", addTodo);
# // router.put("/todo/:todoid", updateTodo);
# // router.delete("/todo/:id", deleteTodo);
# router.put("/:id", updateTodo);
# router.delete("/:id", deleteTodo);


# export default router;










# # index.js
# import express from "express";
# import { connection } from "./postgres/postgres.js";
# import userRouter from "./view/User-routes.js";
# import todoRouter from "./view/Todo-routes.js";
# import cors from "cors";

# const app = express();

# app.use(express.json());
# app.use(cors());
# app.use('/user',userRouter);
# app.use('/todo',todoRouter)


# const PORT = 8000;

# app.listen(PORT, () => {
#   console.log(`Server Is Running ${PORT}`);
# });
# connection();


# # package.json
# {
#   "name": "server",
#   "version": "1.0.0",
#   "description": "",
#   "main": "index.js",
#   "scripts": {
#     "start": "nodemon index.js",
#     "test": "echo \"Error: no test specified\" && exit 1"
#   },
#   "keywords": [],
#   "author": "",
#   "license": "ISC",
#   "type": "module",
#   "dependencies": {
#     "cors": "^2.8.5",
#     "express": "^5.1.0",
#     "nodemon": "^3.1.10",
#     "pg": "^8.16.3",
#     "pg-hstore": "^2.3.4",
#     "sequelize": "^6.37.7"
#   }
# }

