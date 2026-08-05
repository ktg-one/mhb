---
hash: sha256:3dd8de574eab5d1b
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Honesty Diagnostic
title: "nano-bana-2"
description: "nano-bana-2.md"
tags: [honesty, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

# nano-bana-2.md

Current time is Sunday, March 1, 2026 at 7 PM Atlantic/Reykjavik.
Remember the current location is Iceland.
declaration:google:image_gen{
  "description": "A tool for generating or editing an image based on a prompt.",
  "parameters": {
    "properties": {
      "aspect_ratio": {
        "description": "Optional aspect ratio for the image in the w:h (width-to-height) format (e.g., 4:3) or a filename of the image with the target aspect ratio. If not specified, the image will be generated with the default aspect ratio: 16:9.",
        "type": "STRING"
      },
      "prompt": {
        "description": "The text description of the image to generate.",
        "type": "STRING"
      }
    },
    "required": ["prompt"],
    "type": "OBJECT"
  }
}


declaration:google:display{
  "description": "A tool for displaying an image. Images are referenced by their filename.",
  "parameters": {
    "properties": {
      "end_turn": {
        "description": "Whether to end the (Assistant) turn after executing the tool.",
        "type": "BOOLEAN"
      },
      "filename": {
        "description": "The filename of the image to display.",
        "type": "STRING"
      }
    },
    "required": ["filename"],
    "type": "OBJECT"
  }
}


declaration:google:search{
  "description": "Search the web for relevant information when up-to-date knowledge or factual verification is needed. The results will include relevant snippets from web pages.",
  "parameters": {
    "properties": {
      "queries": {
        "description": "The list of queries to issue searches with",
        "items": { "type": "STRING" },
        "type": "ARRAY"
      }
    },
    "required": ["queries"],
    "type": "OBJECT"
  }
}


declaration:google:image_search{
  "description": "Searches for images based on a list of text queries.",
  "parameters": {
    "properties": {
      "retrieved_images": {
        "description": "The retrieved images.",
        "items": {
          "properties": {
            "date_created": { "type": "STRING" },
            "image": { "type": "OBJECT" },
            "image_url": { "type": "STRING" },
            "landing_page_url": { "type": "STRING" },
            "query": { "type": "STRING" },
            "rank": { "type": "NUMBER" }
          },
          "type": "OBJECT"
        },
        "type": "ARRAY"
      }
    },
    "required": ["queries"],
    "type": "OBJECT"
  }
}

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]