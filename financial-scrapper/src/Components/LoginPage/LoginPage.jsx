import React, {useState } from "react";
import './LoginPage.css'
const Login = () => {
    // State to hold the user credentials
    const [credentials, setCredentials] = useState({
      username: '',
      password: '',
    });

  // Function to handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials({
      ...credentials,
      [name]: value,
    });
  };

  // Function to handle form submission
  const handleFormSubmit = (e) => {
    e.preventDefault();
    // You can add authentication logic here, e.g., API calls, etc.
    console.log('Login credentials submitted:', credentials);
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleFormSubmit}>
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={credentials.username}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={credentials.password}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

// Export the Login component
export default Login;