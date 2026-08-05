> [!info] AI Workflow History
> - 7/22/2026, 3:59:40 PM: Created - "Search the folder using fuzzy search or semantic search for the keyword
> - 7/22/2026, 4:26:55 PM: Modified - "You broke the workflow. I want it to search a folder and it keeps asking to search a specific note... here are the terms: input them:
> - 7/22/2026, 4:40:07 PM: Modified - "cement the naming rubrik so  idont get prompted again Date created -><MMDDYYYY>-<Model-Id>-<Title>-<status>"
> - 7/22/2026, 4:46:11 PM: Modified - "fix"
> - 7/22/2026, 4:59:23 PM: Modified - "That completely didn't work. It just completed in two seconds and nothing was done"
> - 7/22/2026, 6:15:39 PM: Modified - "fix plz"
> - 7/22/2026, 6:35:07 PM: Modified - "fix"
> - 7/22/2026, 6:38:07 PM: Modified - "fix plz. probably lint or test it before you give it back"
> - 7/22/2026, 6:40:47 PM: Modified - "fix and test. if it passes u it will pass me pull jq"
> - 7/22/2026, 6:49:40 PM: Modified - "u didnt' test same error"
Search THE VAULT, minus folders
./gemini-rmdre
./context
./.*

To move to folder
/Vault-OKF-Knowledge-Base/LLM_Tests/

Naming Rubrik Date created -><MMDDYYYY>-<Model-Id>-<Title>-<status>"
"## TECHNIQUE HONESTY TABLE" with the findings
- Move them to the respective folder in /OKF
- Split each of the test in half from the [ "Platform Self Assessment" heading ]-> move to Self-Assessment folder
- Rename the file to <naming rubrik"
- log your work"

```workflow
name: Consolidate-01
nodes:
  - id: init-search-folder
    type: variable
    comment: Initialize search folder to empty string for entire vault search.
    name: searchFolder
  - id: init-log
    type: variable
    comment: Initialize an empty JSON array to store log messages as the workflow processes notes.
    name: logEntries
    value: "[]"
  - id: init-index
    type: variable
    comment: Initialize the loop counter to 0 for iterating through the search results.
    name: index
    value: "0"
  - id: init-renaming-rubric
    type: variable
    comment: Define the dynamic renaming rubric, including the requested format.
    name: renamingRubric
    value: Date created -><MMDDYYYY>-<Model-Id>-<Title>-<status>
  - id: init-archive-folder
    type: variable
    comment: Define the target folder for archiving original notes.
    name: archiveFolder
    value: Archive
  - id: search-notes
    type: note-search
    comment: Search for notes containing the exact heading '## TECHNIQUE HONESTY TABLE' across the entire vault.
    query: "## TECHNIQUE HONESTY TABLE"
    searchContent: "true"
    saveTo: foundNotes
  - id: filter-found-notes
    type: script
    comment: "SCRIPT: Filter out notes from specified excluded folders and top-level dot folders. This prevents processing previously archived or moved notes."
    code: |
      var rawNotes = "{{foundNotes:json}}";
      var notes = [];
      if (rawNotes && rawNotes.trim() !== "") {
          try {
              notes = JSON.parse(rawNotes);
          } catch (e) {
              notes = [];
          }
      }
      if (!Array.isArray(notes)) {
          notes = [];
      }

      var filtered = [];
      var excludeFolders = ["gemini-rmdre", "context", "Archive", "Self-Assessment", "Vault-OKF-Knowledge-Base", "Workflow Logs"];

      for (var i = 0; i < notes.length; i++) {
          var note = notes[i];
          if (!note || !note.path) continue;
          var path = note.path;
          var parts = path.split('/');
          var topLevelFolder = parts[0];

          if (excludeFolders.includes(topLevelFolder)) continue;
          if (topLevelFolder.startsWith('.')) continue;

          filtered.push(note);
      }
      return JSON.stringify({ notes: filtered, count: filtered.length });
    saveTo: filteredNotesRaw
  - id: parse-filtered-notes
    type: json
    comment: Parse the filtered notes list JSON string into an accessible object.
    source: filteredNotesRaw
    saveTo: filteredNotes
  - id: loop-through-notes
    type: while
    comment: Loop through each filtered note to process it.
    condition: "{{index}} < {{filteredNotes.count}}"
    trueNext: set-current-note-variables
    falseNext: create-log-note
  - id: set-current-note-variables
    type: set
    comment: Set original note metadata variables for the current iteration.
    name: originalNotePath
    value: "{{filteredNotes.notes[index].path}}"
    next: set-current-note-name
  - id: set-current-note-name
    type: set
    comment: Set the name of the original note for the current iteration.
    name: originalNoteName
    value: "{{filteredNotes.notes[index].name}}"
    next: set-current-note-created
  - id: set-current-note-created
    type: set
    comment: Set the creation timestamp of the original note.
    name: originalNoteCreated
    value: "{{filteredNotes.notes[index].created}}"
    next: prepare-iteration-paths
  - id: prepare-iteration-paths
    type: script
    comment: "SCRIPT: Prepare clean paths without .md extension for note operations, and archive paths."
    code: |
      var rawPath = "{{originalNotePath:json}}";
      var cleanPath = rawPath.endsWith(".md") ? rawPath.slice(0, -3) : rawPath;

      var archiveFolder = "{{archiveFolder:json}}";
      var originalName = "{{originalNoteName:json}}";
      var archiveNotePath = archiveFolder + "/" + originalName;

      return JSON.stringify({
        cleanPath: cleanPath,
        archiveNotePath: archiveNotePath
      });
    saveTo: iterationPathsRaw
    next: parse-iteration-paths
  - id: parse-iteration-paths
    type: json
    comment: Parse the iteration paths JSON string into a helper object.
    source: iterationPathsRaw
    saveTo: paths
    next: read-current-note
  - id: read-current-note
    type: note-read
    comment: Read the entire content of the current note.
    path: "{{originalNotePath}}"
    saveTo: noteContent
    next: determine-okf-folder
  - id: determine-okf-folder
    type: script
    comment: "SCRIPT: Determine the target subfolder within the '/OKF' directory."
    code: |
      return "Vault-OKF-Knowledge-Base/LLM_Tests";
    saveTo: newOKFFolder
    next: process-content
  - id: process-content
    type: script
    comment: "SCRIPT: Process and split the note content in a single step to avoid multiple massive string compilations."
    code: |
      var content = "{{noteContent:json}}";
      var marker = "Platform Self Assessment";
      var index = content.indexOf(marker);
      var found = index >= 0;

      var original = "";
      var selfAssessment = "";

      if (found) {
          original = content.substring(0, index).trim();
          selfAssessment = content.substring(index).trim();
      } else {
          original = content;
      }

      var originalNoteName = "{{originalNoteName:json}}";
      var originalNoteCreatedTimestamp = parseInt("{{originalNoteCreated}}", 10);
      if (isNaN(originalNoteCreatedTimestamp)) {
          originalNoteCreatedTimestamp = Date.now();
      }
      var renamingRubricTemplate = "{{renamingRubric:json}}";

      var date = new Date(originalNoteCreatedTimestamp);
      var mm = String(date.getMonth() + 1).padStart(2, '0');
      var dd = String(date.getDate()).padStart(2, '0');
      var yyyy = date.getFullYear();
      var formattedDate = mm + dd + yyyy;

      var newName = originalNoteName;
      if (found) {
          newName = renamingRubricTemplate;
          newName = newName.replace(/<MMDDYYYY>/g, formattedDate);
          newName = newName.replace(/<Title>/g, originalNoteName);
          newName = newName.replace(/<Model-Id>/g, "unknown-model");
          newName = newName.replace(/<status>/g, "processed");
          newName = newName.replace(/[^a-zA-Z0-9\-_ ]/g, '');
          if (newName.trim() === "") newName = originalNoteName + "-processed";
      }

      var newOKFFolder = "{{newOKFFolder:json}}";
      var newOriginalNotePath = newOKFFolder + "/" + newName;
      var newSelfAssessmentNotePath = "Self-Assessment/" + originalNoteName + " - Platform Self Assessment";

      return JSON.stringify({
          found: found,
          originalContent: original,
          selfAssessmentContent: selfAssessment,
          newOriginalNotePath: newOriginalNotePath,
          newSelfAssessmentNotePath: newSelfAssessmentNotePath
      });
    saveTo: processResultRaw
    next: parse-process-result
  - id: parse-process-result
    type: json
    comment: Parse the process results into an accessible object.
    source: processResultRaw
    saveTo: processResult
    next: check-split-found
  - id: check-split-found
    type: if
    comment: Check if the 'Platform Self Assessment' split marker was detected.
    condition: "{{processResult.found}} == true"
    trueNext: create-self-assessment-note
    falseNext: write-original-note
  - id: create-self-assessment-note
    type: note
    comment: Create the new note in the 'Self-Assessment' folder.
    path: "{{processResult.newSelfAssessmentNotePath}}"
    content: "{{processResult.selfAssessmentContent}}"
    mode: create
    confirm: "false"
    next: write-original-note
  - id: write-original-note
    type: note
    comment: Save the modified content (before split or whole note) to the OKF folder.
    path: "{{processResult.newOriginalNotePath}}"
    content: "{{processResult.originalContent}}"
    mode: overwrite
    confirm: "false"
    next: archive-original-note
  - id: archive-original-note
    type: note
    comment: Save original copy of note in Archive folder.
    path: "{{paths.archiveNotePath}}"
    content: "{{noteContent}}"
    mode: overwrite
    confirm: "false"
    next: clear-original-note
  - id: clear-original-note
    type: note
    comment: Clear original source note's content so it is not parsed or matched again.
    path: "{{paths.cleanPath}}"
    content: This note has been processed, split, and archived.
    mode: overwrite
    confirm: "false"
    next: check-log-type
  - id: check-log-type
    type: if
    comment: Check if the note was split or just moved to determine logging content.
    condition: "{{processResult.found}} == true"
    trueNext: log-processed-note
    falseNext: log-moved-only-note
  - id: log-processed-note
    type: script
    comment: "SCRIPT: Add details about successful split and process to log."
    code: |
      var log = JSON.parse("{{logEntries:json}}");
      log.push("- Processed '{{originalNotePath:json}}': Split content. Renamed original to '{{processResult.newOriginalNotePath:json}}'. Self-Assessment created at '{{processResult.newSelfAssessmentNotePath:json}}'. Original copy archived.");
      return JSON.stringify(log);
    saveTo: logEntries
    next: increment-index
  - id: log-moved-only-note
    type: script
    comment: "SCRIPT: Add details about the note being moved without splitting to the log."
    code: |
      var log = JSON.parse("{{logEntries:json}}");
      log.push("- Moved '{{originalNotePath:json}}' to '{{processResult.newOriginalNotePath:json}}' (no 'Platform Self Assessment' section found). Original copy archived.");
      return JSON.stringify(log);
    saveTo: logEntries
    next: increment-index
  - id: increment-index
    type: set
    comment: Increment the loop counter to proceed to the next note in the search results.
    name: index
    value: "{{index}} + 1"
    next: loop-through-notes
  - id: create-log-note
    type: script
    comment: "SCRIPT: Compile all collected log entries into a single Markdown string for the final log note."
    code: |
      var log = JSON.parse("{{logEntries:json}}");
      var logContent = "# Workflow Log: Consolidate-01\n\n";
      logContent += "Executed: " + new Date().toLocaleString() + "\n";
      logContent += "Renaming Rubric: " + "{{renamingRubric:json}}" + "\n\n";
      if (log.length === 0) {
          logContent += "No relevant notes found for processing, or all were filtered out.\n";
      } else {
          logContent += "## Changes Made:\n";
          log.forEach(function(entry) {
              logContent += entry + "\n";
          });
      }
      return logContent;
    saveTo: finalLogContent
    next: generate-log-path
  - id: generate-log-path
    type: script
    comment: "SCRIPT: Generate the unique log file path with a timestamp."
    code: |
      return "Workflow Logs/Consolidate-01 Log - " + new Date().toISOString().slice(0, 16).replace('T', ' ').replace(/:/g, '-');
    saveTo: logFilePath
    next: save-log-note
  - id: save-log-note
    type: note
    comment: Save the generated log content as a new note in a 'Workflow Logs' folder.
    path: "{{logFilePath}}"
    content: "{{finalLogContent}}"
    mode: create
    confirm: "false"
    next: end-dialog
  - id: end-dialog
    type: dialog
    comment: Display completion dialog to user.
    title: Workflow Complete
    message: Consolidate-01 workflow finished processing notes. Check the log note in 'Workflow Logs' folder for details.
    next: end
```