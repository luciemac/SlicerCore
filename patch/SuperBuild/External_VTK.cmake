# With SlicerCore, vtk is always external
# Slicer does a find_package VTK that fails on Windows due to RenderingOpenXR module dependency
# c.f. https://gitlab.kitware.com/vtk/vtk/-/merge_requests/12363
ExternalProject_Add_Empty(VTK)
