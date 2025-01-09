import React, { useState } from "react";

const Diary = ({ onSubmit }) => {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(text);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        rows="5"
        placeholder="Write your daily diary reflection..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button type="submit">Analyze Diary</button>
    </form>
  );
};

export default Diary;
