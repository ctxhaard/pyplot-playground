 let
  pkgs = import <nixpkgs> {};
in
  with pkgs;
  mkShell {
    name = "matplotlib-playground";
    packages = [
      (python3.withPackages (p: [p.numpy p.matplotlib]))
    ];
  }
