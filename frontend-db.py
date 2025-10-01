# page.tsx
# import React from "react";
# import TodoApp from "./Todos/page";

# function Page() {
#   return (
#     <div>
#       <TodoApp />
#     </div>
#   );
# }
# export default Page;


# Todos --> page.tsx
# "use client"; // important for Next.js client component

# import { useEffect, useState } from "react";
# import axios from "axios";
# import { ImPlus } from "react-icons/im";
# import { MdOutlineEdit, MdDelete } from "react-icons/md";

# function TodoApp() {
#   const [newTask, setNewTask] = useState("");
#   const [tasks, setTasks] = useState<any[]>([]);
#   const [editId, setEditId] = useState<number | null>(null);

#   // ✅ Step 1: Load tasks from API
#   useEffect(() => {
#     fetchTasks();
#   }, []);

#   const fetchTasks = async () => {
#     try {
#       const res = await axios.get("http://localhost:8000/todo/getAll");
#       console.log("📌 Backend Response:", res.data);

#       if (Array.isArray(res.data)) {
#         setTasks(res.data); // agar array hai to use karo
#       } else {
#         setTasks([]); // agar object (error) mila to empty array
#       }
#     } catch (err) {
#       console.error("Error fetching todos:", err);
#       setTasks([]); // error case me bhi safe array
#     }
#   };

#   // ✅ Step 2: Add / Update Task
#   const addTask = async () => {
#     if (newTask.trim() === "") return;

#     try {
#       if (editId !== null) {
#         // Update Task
#         await axios.put(`http://localhost:8000/todo/${editId}`, {
#           name: newTask,
#         });
#       } else {
#         // Add Task
#         await axios.post("http://localhost:8000/todo/addTodo", {
#           name: newTask,
#         });
#       }

#       setNewTask("");
#       setEditId(null);
#       fetchTasks(); // Refresh list
#     } catch (err) {
#       console.error("Error saving task:", err);
#     }
#   };

#   // ✅ Step 3: Delete Task
#   const deleteTask = async (id: number) => {
#     try {
#       await axios.delete(`http://localhost:8000/todo/${id}`);
#       fetchTasks();
#     } catch (err) {
#       console.error("Error deleting task:", err);
#     }
#   };

#   // ✅ Step 4: Edit Task
#   const editTask = (task: any) => {
#     setNewTask(task.name);
#     setEditId(task.id);
#   };

#   return (
#     <div className="w-full min-h-screen bg-[#020817] flex flex-col items-center px-4">
#       {/* Header */}
#       <div className="w-full max-w-2xl mx-auto h-18 mt-14 bg-[#162C17] rounded-lg flex items-center">
#         <h1 className="w-full max-w-2xl mx-auto ml-6 text-4xl text-[#CEFF45] font-extrabold">
#           TODO
#         </h1>
#       </div>

#       {/* Input Box */}
#       <div className="w-full max-w-2xl mx-auto bg-[#7EAC01] h-24 mt-4 flex flex-wrap md:flex-nowrap items-center rounded-lg p-4 gap-3">
#         <input
#           type="text"
#           placeholder="Type Your Task Here...."
#           value={newTask}
#           onChange={(e) => setNewTask(e.target.value)}
#           className="flex-1 min-w-[200px] md:w-[400px] h-16 bg-gray-100 text-black rounded-full font-semibold px-4"
#         />

#         <button
#           onClick={addTask}
#           className="w-12 h-12 bg-[#162C17] text-white rounded-lg shadow hover:bg-[#CFF46] flex items-center justify-center"
#         >
#           <ImPlus size={24} />
#         </button>
#       </div>

#       {/* Tasks List */}
#       {tasks.length > 0 ? (
#         tasks.map((task) => (
#           <div
#             key={task.id}
#             className="w-full max-w-2xl mx-auto h-18 mt-3 bg-[#162C17] rounded-lg flex items-center justify-between px-4"
#           >
#             <span className="text-2xl text-[#CEFF45] font-semibold ">
#               {task.name}
#             </span>

#             <div className="flex gap-3">
#               {/* Edit Button */}
#               <span
#                 onClick={() => editTask(task)}
#                 className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white cursor-pointer"
#               >
#                 <MdOutlineEdit size={24} />
#               </span>

#               {/* Delete Button */}
#               <span
#                 onClick={() => deleteTask(task.id)}
#                 className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-red-500 rounded-lg text-white cursor-pointer"
#               >
#                 <MdDelete size={20} />
#               </span>
#             </div>
#           </div>
#         ))
#       ) : (
#         <p className="text-white mt-4">No tasks found</p>
#       )}
#     </div>
#   );
# }

# export default TodoApp;

