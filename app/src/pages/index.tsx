import { useState } from "react";
import { invoke } from "@tauri-apps/api/tauri";
import Image from "next/image";
import Navbar from "../components/navbar";

export default function App() {

  return (
    <div className="container">
      <Navbar/>
    </div>
  );
}
