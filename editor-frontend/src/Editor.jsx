import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import { useState, useEffect } from "react";
import { generateHTML } from "@tiptap/core";

export default function Editor() {
  const [title, setTitle] = useState("");
  const [outputHTML, setOutputHTML] = useState("");

  const editor = useEditor({
    extensions: [StarterKit],
    content: "<p>Hello Tiptap 👋</p>",
    onUpdate: ({ editor }) => {
      const json = editor.getJSON();
      const html = generateHTML(json, [StarterKit]);
      setOutputHTML(html);
    },
  });

  const saveTemplate = async () => {
    const payload = {
      title,
      content: editor.getJSON(),
    };

    await fetch("http://localhost:5000/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    alert("Template saved!");
  };

  if (!editor) return null;

  return (
    <div className="editor-container">
      <input
        placeholder="Template title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      {/* Toolbar */}
      <div className="toolbar">
        <button
          onClick={() => editor.chain().focus().toggleBold().run()}
          className={editor.isActive("bold") ? "active" : ""}
        >
          Bold
        </button>

        <button
          onClick={() => editor.chain().focus().toggleItalic().run()}
          className={editor.isActive("italic") ? "active" : ""}
        >
          Italic
        </button>
      </div>

      {/* Editor */}
      <EditorContent editor={editor} className="editor-content" />

      {/* Save */}
      <button onClick={saveTemplate} className="save-button">
        Save as Templates
      </button>

      {/* OUTPUT PREVIEW */}
      <div className="output-container">
        <h3>Output HTML</h3>
        <div
          className="output"
          dangerouslySetInnerHTML={{ __html: outputHTML }}
        />
      </div>
    </div>
  );
}