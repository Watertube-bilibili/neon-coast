"""Verify and unpack only the manifest-listed public runtime files."""
import hashlib,json,pathlib,stat,zipfile
root=pathlib.Path(__file__).resolve().parent
manifest=json.loads((root/'release-manifest.json').read_text())
assert manifest['version']==1
out=root/'_site';out.mkdir(exist_ok=True)
seen=set()
for archive in manifest['archives']:
 path=root/archive['file']
 assert path.stat().st_size==archive['bytes']
 assert hashlib.sha256(path.read_bytes()).hexdigest()==archive['sha256']
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  for info in z.infolist():
   name=info.filename;parts=pathlib.PurePosixPath(name).parts
   assert not info.is_dir() and not stat.S_ISLNK(info.external_attr>>16)
   assert name in manifest['files'] and name not in seen
   assert not name.startswith('/') and '..' not in parts
   assert not any(p in {'.git','.openai','.sites-runtime','node_modules'} for p in parts)
   data=z.read(info);expected=manifest['files'][name]
   assert len(data)==expected['bytes'] and hashlib.sha256(data).hexdigest()==expected['sha256'],name
   dest=out/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data);seen.add(name)
assert seen==set(manifest['files'])
assert {str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()}==seen
assert (out/'index.html').is_file() and (out/'preview-1-5/index.html').is_file()
print(f'Verified {len(seen)} runtime files; source {manifest["originalSourceCommit"]}; formal {manifest["formalVersion"]}; preview {manifest["previewVersion"]}.')
