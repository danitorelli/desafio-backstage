import streamlit as st

def main():
    st.title("Exemplos de Linguagens de Programção")

    languages = {
        "Python": {
            "example": "print('Hello, World!')",
            "documentation": "https://docs.python.org/3/"
        },
        "Go (Golang)": {
            "example": 'package main\n\nimport "fmt"\n\nfunc main() {\n    fmt.Println("Hello, World!")\n}',
            "documentation": "https://golang.org/doc/"
        },
        "Java": {
            "example": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
            "documentation": "https://docs.oracle.com/en/java/"
        },
        "Ruby": {
            "example": 'puts "Hello, World!"',
            "documentation": "https://ruby-doc.org/core-3.0.2/"
        },
        "Swift": {
            "example": 'import Swift\nprint("Hello, World!")',
            "documentation": "https://docs.swift.org/swift-book/"
        }
    }

    selected_language = st.selectbox("Selecione a Linguagem de Programação:", list(languages.keys()))
    example_code = languages[selected_language]["example"]
    documentation_link = languages[selected_language]["documentation"]

    st.write(f"**Código de exemplo**:\n```{selected_language}\n{example_code}\n```")
    st.write(f"**Documentação da linguagem**: [Link]({documentation_link})")

if __name__ == "__main__":
    main()
