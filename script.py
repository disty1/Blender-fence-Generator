"""
SOAL 1
===============================================================
Membuat 1 objek pagar (silinder panjang + kerucut tajam di ujungnya)
lalu menduplikasi objek tersebut sehingga menjadi 8 buah pagar
yang tersusun lurus seperti pagar halaman.

Langkah yang dilakukan script ini:
1. Membersihkan objek lama yang memakai nama "FenceUnit".
2. Membuat silinder (batang pagar).
3. Membuat kerucut (ujung runcing pagar).
4. Menyatukan (join) silinder + kerucut menjadi 1 objek.
5. Mengatur tinggi (height) silinder dan kerucut.
6. Mengatur radius silinder.
7. Mengatur posisi objek.
8. Menduplicate menjadi 8 unit pagar.
9. Menyusun pagar secara rapi menggunakan SPACING.

Script ini HANYA mengerjakan bagian modeling untuk SKENARIO SOAL 1.
"""

import bpy

# -------------------------
# PARAMETER MODEL PAGAR
# -------------------------
NUM_UNITS = 8               # jumlah pagar
CYLINDER_HEIGHT = 3.0       # tinggi silinder
CYLINDER_RADIUS = 0.1       # radius silinder
CONE_HEIGHT = 0.5           # tinggi kerucut
SPACING = 0.4               # jarak antar pagar

# -------------------------
# HAPUS OBJEK LAMA (AMAN)
# -------------------------
for o in bpy.data.objects:
    if o.name.startswith("FenceUnit"):
        bpy.data.objects.remove(o, do_unlink=True)

# -------------------------
# MEMBUAT SILINDER
# -------------------------
bpy.ops.mesh.primitive_cylinder_add(
    radius=CYLINDER_RADIUS,
    depth=CYLINDER_HEIGHT,
    location=(0, 0, CYLINDER_HEIGHT / 2)
)
cyl = bpy.context.active_object
cyl.name = "FenceUnit_Cylinder"


# -------------------------
# MEMBUAT KERUCUT (UJUNG TAJAM)
# -------------------------
bpy.ops.mesh.primitive_cone_add(
    radius1=CYLINDER_RADIUS,
    radius2=0,
    depth=CONE_HEIGHT,
    location=(0, 0, CYLINDER_HEIGHT + (CONE_HEIGHT / 2))
)
cone = bpy.context.active_object
cone.name = "FenceUnit_Cone"

# join jadi satu objek
bpy.ops.object.select_all(action='DESELECT')
cyl.select_set(True)
cone.select_set(True)
bpy.context.view_layer.objects.active = cyl
bpy.ops.object.join()
unit = bpy.context.active_object
unit.name = "FenceUnit_01"

# -------------------------
# DUplikasi pagar menjadi 8
# -------------------------
for i in range(1, NUM_UNITS):
    new = unit.copy()
    new.data = unit.data.copy()
    new.location = (i * SPACING, 0, 0)
    new.name = f"FenceUnit_{i+1:02d}"
    bpy.context.collection.objects.link(new)

print("SOAL 1 SELESAI — 8 pagar berhasil dibuat.")
