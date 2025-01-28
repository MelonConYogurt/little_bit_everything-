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
import {BookOpen} from "lucide-react";
import {getCount} from "@/utils/count";

export default function TableBooks() {
  const [data, setData] = useState<Book[]>([]);
  const [count, setCount] = useState(0);
  const [limit, setLimit] = useState(10);
  const [offset, setOffset] = useState(0);
  const [page, setPage] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      const dataOfBooks = await getDataBooks(limit, offset);
      if (dataOfBooks?.data) {
        setData(dataOfBooks.data);
      }
    };
    fetchData();
  }, [limit, offset]);

  useEffect(() => {
    const fetchCount = async () => {
      const DataOfCount = await getCount();
      setCount(DataOfCount.pages);
    };
    fetchCount();
  }, []);

  function PageUp() {
    setPage((prev) => {
      const newPage = prev + 1;
      setOffset((newPage - 1) * limit);
      return newPage;
    });
  }

  function PageDown() {
    setPage((prev) => {
      const newPage = prev - 1;
      setOffset((newPage - 1) * limit);
      return newPage;
    });
  }

  return (
    <div className="flex flex-col min-h-screen">
      <header className="border-b">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <div className="flex justify-center items-center gap-2">
            <Button disabled={page <= 1} onClick={() => PageDown()}>
              Atras
            </Button>
            <form action="">
              <Input
                onChange={(e) => setPage(Number(e.target.value))}
                type="number"
                placeholder={page.toString()}
              ></Input>
              <p>/ de {Math.ceil(count / limit)}</p>
            </form>
            <Button
              disabled={page >= Math.ceil(count / limit)}
              onClick={() => PageUp()}
            >
              Adelante
            </Button>
          </div>
          <div className="flex items-center gap-4">
            <div className="relative flex gap-2 mx-5">
              <h3>Hay un total de {count} libros</h3>
            </div>
            <div className="flex justify-center items-center">
              <form className="flex justify-center items-center">
                <label>Limite de filas actual: {limit}</label>
                <Input
                  onChange={(e) => setLimit(Number(e.target.value))}
                  type="number"
                  placeholder={limit.toString()}
                ></Input>
              </form>
            </div>
          </div>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="flex-1 justify-center items-center">
          <h1 className="text-2xl font-bold flex items-center gap-2">
            <BookOpen className="h-6 w-6" />
            Biblioteca Modernas
          </h1>
        </div>
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
    </div>
  );
}
