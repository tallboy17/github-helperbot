Repository: deepspeedai/DeepSpeed
Language: Python
Stars: 39026
Forks: 4426
-----
Many DeepSpeed features are supported on Windows for both training and inference. You can read more about this in the original blog post [here](https://github.com/deepspeedai/DeepSpeed/tree/master/blogs/windows/08-2024/README.md). Among features that are currently not supported are async io (AIO) and GDS (which does not support Windows).
1. Install PyTorch, such as pytorch 2.3+cu121.
2. Install Visual C++ build tools, such as VS2022 C++ x64/x86 build tools.
3. Launch Cmd console with Administrator permissions for creating required symlink folders and ensure MSVC tools are added to your PATH or launch the Developer Command Prompt for Visual Studio 2022 with administrator permissions.
4. Run `build_win.bat` to build wheel in `dist` folder.