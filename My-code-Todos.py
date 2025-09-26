# My own code 
"use client";
import { useState , useEffect} from "react";
import { FaPlus } from "react-icons/fa6";
import { ImPlus } from "react-icons/im";
import { MdOutlineEdit } from "react-icons/md";
import { MdDelete } from "react-icons/md";

// function TodoApp() {
//   const [isChecked, setIsChecked] = useState(false);
//   const [count, setCount] = useState(0);

//   return (
//     <div className="w-full min-h-screen bg-[#020817] flex flex-col items-center px-4 ">
//       <div className="w-full  max-w-2xl mx-auto h-18 mt-14 bg-[#162C17] rounded-lg flex items-center ">
//         <input
//           type="checkbox"
//           checked={isChecked}
//           onChange={(e) => setIsChecked(e.target.checked)}
//           className="w-7 h-7 ml-10 rounded-2xl"
//         />

//         <div className="w-full  max-w-2xl mx-auto text-4xl text-[#CEFF45] justify-center  font-extrabold ml-6">
//           TODO
//         </div>
//       </div>

//       <div className="w-full max-w-2xl mx-auto bg-[#7EAC01] h-24 mt-2 flex flex-wrap md:flex-nowrap items-center rounded-lg p-4 gap-3 ">
//         <input
//           type="text"
//           placeholder="Type Your Task Here..."
//           className=" flex-1 min-w-[200px] md:w-[400px] h-16 bg-gray-100 text-black rounded-full font-semibold px-4"
//         />

//         <button
//           onClick={() => setCount(count + 1)}
//           className="w-12 h-12 bg-[#162C17] text-white rounded-lg shadow hover:bg-[#CFFF46] flex items-center justify-center"
//         >
//           <ImPlus size={24} />
//         </button>

//         <button
//           onClick={() => setCount(count - 1)}
//           className="w-12 h-12 bg-[#162C17] text-white rounded-lg shadow hover:bg-[#CFFF46] flex items-center justify-center"
//         >
//           <MdOutlineEdit size={24} />
//         </button>

//         <button
//           onClick={() => setCount(count - 1)}
//           className="w-12 h-12 bg-[#162C17] text-white rounded-lg shadow hover:bg-[#CFFF46] flex items-center justify-center"
//         >
//           <MdDelete size={24} />
//         </button>
//       </div>

//       <div className="w-full  max-w-2xl mx-auto h-18 mt-14 bg-[#162C17] rounded-lg flex items-center justify-between  ">
//         <input
//           type="checkbox"
//           checked={isChecked}
//           onChange={(e) => setIsChecked(e.target.checked)}
//           className="w-7 h-7 ml-10 rounded-2xl"
//         />

//         <div className="w-full max-w-2xl mx-auto text-4xl text-[#CEFF45] flex items-center justify-between font-semibold ml-6">
//           <span>Task</span>

//           <div className="flex gap-3 mr-6">
//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdOutlineEdit size={24} />
//             </span>

//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdDelete size={20} />
//             </span>
//           </div>
//         </div>
//       </div>

//       <div className="w-full  max-w-2xl mx-auto h-18 mt-2 bg-[#162C17] rounded-lg flex items-center ">
//         <input
//           type="checkbox"
//           checked={isChecked}
//           onChange={(e) => setIsChecked(e.target.checked)}
//           className="w-7 h-7 ml-10 rounded-2xl"
//         />

//         <div className="w-full max-w-2xl mx-auto text-4xl text-[#CEFF45] flex items-center justify-between font-semibold ml-6">
//           <span>Task</span>

//           <div className="flex gap-3 mr-6">
//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdOutlineEdit size={24} />
//             </span>

//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdDelete size={20} />
//             </span>
//           </div>
//         </div>
//       </div>

//       <div className="w-full  max-w-2xl mx-auto  h-18 mt-2 bg-[#162C17] rounded-lg flex items-center ">
//         <input
//           type="checkbox"
//           checked={isChecked}
//           onChange={(e) => setIsChecked(e.target.checked)}
//           className="w-7 h-7 ml-10 rounded-2xl"
//         />

//         <div className="w-full max-w-2xl mx-auto text-4xl text-[#CEFF45] flex items-center justify-between font-semibold ml-6">
//           <span>Task</span>

//           <div className="flex gap-3 mr-6">
//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdOutlineEdit size={24} />
//             </span>

//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdDelete size={20} />
//             </span>
//           </div>
//         </div>
//       </div>

//       <div className="w-full  max-w-2xl mx-auto h-18 mt-2 bg-[#162C17] rounded-lg flex items-center ">
//         <input
//           type="checkbox"
//           checked={isChecked}
//           onChange={(e) => setIsChecked(e.target.checked)}
//           className="w-7 h-7 ml-10 rounded-2xl"
//         />

//         <div className="w-full max-w-2xl mx-auto text-4xl text-[#CEFF45] flex items-center justify-between font-semibold ml-6">
//           <span>Task</span>

//           <div className="flex gap-3 mr-6">
//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdOutlineEdit size={24} />
//             </span>

//             <span className="w-10 h-10 flex items-center justify-center bg-[#7EAC01] hover:bg-[#CFFF46] rounded-lg text-white">
//               <MdDelete size={20} />
//             </span>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }
// export default TodoApp;

