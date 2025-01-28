"use client";

import {useState, useEffect} from "react";
import {getDataBooks, Book} from "@/utils/get";

import {Button} from "@/components/ui/button";
import {Input} from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {BookOpen, Search} from "lucide-react";

export default function TableBooks() {
  const [data, setData] = useState<Book[]>([]); // Tipado del estado

  useEffect(() => {
    const fetchData = async () => {
      const dataOfBooks = await getDataBooks();
      if (dataOfBooks?.data) {
        setData(dataOfBooks.data); // Aseguramos que `data` existe
      }
    };
    fetchData();
  }, []);

  return (
    <div className="flex flex-col min-h-screen">
      <header className="border-b">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <h1 className="text-2xl font-bold flex items-center gap-2">
            <BookOpen className="h-6 w-6" />
            Biblioteca Moderna
          </h1>
          <div className="flex justify-center items-center gap-2">
            <Button>Atras</Button>
            <p>
              Pagina actual: {} / de {}
            </p>
            <Button>Adelante</Button>
          </div>
          <div className="flex items-center gap-4">
            <div className="relative flex gap-2 mx-5">
              <Search className="absolute left-2 top-1/2 transform -translate-y-1/2 text-gray-400" />
              <Input className="pl-8" placeholder="Buscar libros..." />
              <Button>Aceptar</Button>
            </div>
          </div>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="rounded-lg border shadow-sm">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Nombre</TableHead>
                <TableHead>Año</TableHead>
                <TableHead>Autor</TableHead>
                <TableHead>ISBN</TableHead>
                <TableHead>Estado</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {data.length > 0 ? (
                data.map((book, index) => (
                  <TableRow key={index}>
                    <TableCell className="font-medium">{book.name}</TableCell>
                    <TableCell>{book.age}</TableCell>
                    <TableCell>{book.author}</TableCell>
                    <TableCell>{book.isbn}</TableCell>
                    <TableCell>
                      <span className="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">
                        Disponible
                      </span>
                    </TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow></TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </main>

      <footer className="border-t">
        <div className="container mx-auto px-4 py-6 text-center text-sm text-gray-500">
          © 2025 Biblioteca Moderna. Todos los derechos reservados.
        </div>
      </footer>
    </div>
  );
}
