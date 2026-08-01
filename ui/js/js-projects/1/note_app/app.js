// Select elements
const noteInput = document.getElementById("notetxt");
const addBtn = document.getElementById("add_btn");
const notesList = document.getElementById("notes-list");

// Function to create a single note element
function createNote(content) {
  const noteDiv = document.createElement("div");
  noteDiv.classList.add("note");

  noteDiv.innerHTML = `
    <p>${content}</p>
    <button class="delete-btn">Delete</button>
  `;

  // Delete note event
  noteDiv.querySelector(".delete-btn").addEventListener("click", () => {
    noteDiv.remove();
    saveNotes();
  });

  return noteDiv;
}

// Add note on button click
addBtn.addEventListener("click", () => {
  const content = noteInput.value.trim();
  if (content === "") {
    alert("Please write something!");
    return;
  }

  const note = createNote(content);
  notesList.appendChild(note);

  noteInput.value = ""; // clear input
  saveNotes();
});

// Save all notes to localStorage
function saveNotes() {
  const allNotes = [...document.querySelectorAll(".note p")].map(
    (note) => note.textContent
  );
  localStorage.setItem("notes", JSON.stringify(allNotes));
}

// Load saved notes from localStorage
function loadNotes() {
  const savedNotes = JSON.parse(localStorage.getItem("notes")) || [];
  savedNotes.forEach((content) => {
    const note = createNote(content);
    notesList.appendChild(note);
  });
}

// Load notes when page starts
loadNotes();
