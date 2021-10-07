package main

import (
	"flag"
	"log"
	"net/http"
)

type Server struct {
	port string
}

func (s *Server) Run() {
	log.Printf("start server on localhost%s", s.port)

	h1 := func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, there\n"))
	}
	http.HandleFunc("/", h1)
	http.ListenAndServe(s.port, nil)
}

func NewServer(port string) *Server {
	s := Server{port: port}
	return &s
}

func main() {
	port := flag.String("port", ":8080", "server port")
	flag.Parse()

	s := NewServer(*port)
	s.Run()
}
