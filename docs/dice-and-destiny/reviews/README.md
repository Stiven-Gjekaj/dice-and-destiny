# Review requests

The orchestrator session cannot receive messages from the workstream
sessions (it is limited to the trusted devices of the human). A workstream
session asks for a review with a file in this folder.

## How to ask for a review

1. Make the batch. Run `compendium/build.sh`. It must pass. Do not commit the
   batch.
2. Write the review message (the same text that you would send to the
   orchestrator) in a new file in this folder:
   `docs/dice-and-destiny/reviews/<workstream>-<short name of the batch>.md`.
   Example: `bestiary-swamp.md`.
3. Commit only that file: `docs: ask for a review of <batch>`. Push it.
4. Wait. The orchestrator watches this folder. It answers with a message to
   your session.
5. When the batch is approved, commit and push the batch as before.

The orchestrator can still send messages to your session. Do not use
`send_message` to the orchestrator: the server refuses it.
