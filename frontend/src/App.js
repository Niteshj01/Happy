import React, { useState, useEffect } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import AdminLogin from "./components/AdminLogin";
import AdminPanel from "./components/AdminPanel";
import { Toaster } from "./components/ui/sonner";

function App() {
  const [isAdminAuthenticated, setIsAdminAuthenticated] = useState(false);

  useEffect(() => {
    const adminAuth = localStorage.getItem('adminAuth');
    if (adminAuth === 'true') {
      setIsAdminAuthenticated(true);
    }
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route 
            path="/admin" 
            element={
              isAdminAuthenticated ? (
                <AdminPanel onLogout={setIsAdminAuthenticated} />
              ) : (
                <AdminLogin onLogin={setIsAdminAuthenticated} />
              )
            } 
          />
        </Routes>
      </BrowserRouter>
      <Toaster position="top-right" />
    </div>
  );
}

export default App;
