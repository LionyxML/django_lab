import React, { Component, useState, useEffect } from "react";

import {
  BrowserRouter,
  Switch,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

const List = () => {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    try {
      const posts = await fetch("http://localhost:8000/todo");
      const postsJSON = await posts.json();
      setPosts(postsJSON);
    } catch {
      setPosts([{ id: 0, title: "error" }]);
    }
  };

  const sendPost = async () => {
    try {
      await fetch("http://localhost:8000/todo/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: "heeey!" }),
      });

      await fetchPosts();
    } catch {
      alert("Post Error!");
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <>
      <p>These are all the posts!</p>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            ({post?.id}) --- {post?.title}
          </li>
        ))}
      </ul>
      <button onClick={sendPost}>Post another!</button>
    </>
  );
};

export default () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<List />} />
      </Routes>
    </BrowserRouter>
  );
};
