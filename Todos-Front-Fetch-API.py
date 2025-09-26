

"use client";
// Fetch API

import { useEffect, useState } from "react";
import { ImPlus } from "react-icons/im";
import { MdOutlineEdit, MdDelete } from "react-icons/md";

function TodoApp() {
  const [newTask, setNewTask] = useState("");
  const [tasks, setTasks] = useState<string[]>([]);
  const [editIndex, setEditIndex] = useState<number | null>(null);

  // ✅ 1: Load tasks from backend
  useEffect(() => {
    fetch("http://localhost:5000/api/tasks")
      .then((res) => res.json())
      .then((data) => setTasks(data))
      .catch((err) => console.error("Error loading tasks:", err));
  }, []);

  // ✅ 2: Add / Update task
  const addTask = () => {
    if (newTask.trim() === "") return;

    if (editIndex !== null) {
      // Update task
      fetch(`http://localhost:5000/api/tasks/${editIndex}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: newTask }),
      })
        .then((res) => res.json())
        .then((data) => {
          setTasks(data);
          setEditIndex(null);
          setNewTask("");
        });
    } else {
      // Add new task
      fetch("http://localhost:5000/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: newTask }),
      })
        .then((res) => res.json())
        .then((data) => {
          setTasks(data);
          setNewTask("");
        });
    }
  };

  // ✅ 3: Delete task
  const deleteTask = (index: number) => {
    fetch(`http://localhost:5000/api/tasks/${index}`, {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then((data) => setTasks(data));
  };

  // ✅ 4: Edit task
  const editTask = (index: number) => {
    setNewTask(tasks[index]);
    setEditIndex(index);
  };

  return (
    <div className="w-full min-h-screen bg-[#020817] flex flex-col items-center px-4">
      <div className="w-full max-w-2xl mx-auto h-18 mt-14 bg-[#162C17] rounded-lg flex items-center">
        <h1 className="w-full max-w-2xl mx-auto ml-6 text-4xl text-[#CEFF45] font-extrabold">TODO</h1>
      </div>

      <div className="w-full max-w-2xl mx-auto bg-[#7EAC01] h-24 mt-4 flex flex-wrap md:flex-nowrap items-center rounded-lg p-4 gap-3">
        <input
          type="text"
          placeholder="Type Your Task Here...."
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          className="flex-1 min-w-[200px] md:w-[400px] h-16 bg-gray-100 text-black rounded-full font-semibold px-4"
        />

        <button
          onClick={addTask}
          className="w-12 h-12 bg-[#162C17] text-white rounded-lg shadow hover:bg-[#CFF46] flex items-center justify-center"
        >
          <ImPlus size={24} />
        </button>
      </div>

      {tasks.map((task, index) => (
        <div
          key={index}
          className="w-full max-w-2xl mx-auto h-18 mt-3 bg-[#162C17] rounded-lg flex items-center justify-between px-4"
        >
          <span className="text-2xl text-[#CEFF45] font-semibold">
            {task}
          </span>

          <div className="flex gap-3">
            <span
              onClick={() => editTask(index)}
              className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white cursor-pointer"
            >
              <MdOutlineEdit size={24} />
            </span>

            <span
              onClick={() => deleteTask(index)}
              className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-red-500 rounded-lg text-white cursor-pointer"
            >
              <MdDelete size={20} />
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}

export default TodoApp;

Packge.json

{
  "name": "my-app",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build --turbopack",
    "start": "next start",
    "lint": "eslint",
    "server": "node server/server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^5.1.0",
    "next": "15.5.4",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "react-icons": "^5.5.0"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.5.4",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}

