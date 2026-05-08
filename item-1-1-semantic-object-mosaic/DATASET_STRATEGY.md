# Dataset Strategy

## Demo dataset
Use public labeled/segmentation datasets.

Recommended:
- MS COCO val subset for object masks and labels.
- Imagenette only as simple baseline.

## Production direction
- User photos become tile pool.
- Target may be user-uploaded or template.
- If user photos lack background coverage, recommend generated/acquired filler tiles rather than recoloring memories.

## Public/private rule
Only public dataset derivatives may go under `docs/`. Private user or Drive images stay local or ignored.
