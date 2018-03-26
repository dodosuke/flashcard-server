package main

import (
	"io"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/json", json)

	http.ListenAndServe(":8080", nil)
}

func json(w http.ResponseWriter, r *http.Request) {
	f, e := os.Open("./src/output.json")
	if e != nil {
		http.Error(w, "file not found", 404)
		return
	}
	defer f.Close()

	io.Copy(w, f)
}
