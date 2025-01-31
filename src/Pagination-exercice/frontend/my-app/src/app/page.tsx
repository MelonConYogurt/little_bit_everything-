"use client";

import {useState, useEffect} from "react";
import {type Filter, getDataBooks, type Book} from "@/utils/get";
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
import {
  BookOpen,
  ChevronLeft,
  ChevronRight,
  ChevronUp,
  ChevronDown,
} from "lucide-react";
import {getCount} from "@/utils/count";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

export default function TableBooks() {
  const [data, setData] = useState<Book[]>([]);
  const [count, setCount] = useState(0);
  const [limit, setLimit] = useState(10);
  const [offset, setOffset] = useState(0);
  const [page, setPage] = useState(1);
  const [isLoading, setIsLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState<Filter>({
    name: null,
    age: null,
    author: null,
    isbn: null,
  });
  const [selectedBook, setSelectedBook] = useState<Book | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      const dataOfBooks = await getDataBooks(filter, limit, offset, search);
      if (dataOfBooks?.data) {
        setData(dataOfBooks.data);
      }
      setIsLoading(false);
    };
    fetchData();
  }, [limit, offset, filter, search]);

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

  function ManualPage(page: number) {
    if (page > 0 && page <= Math.ceil(count / limit)) {
      setPage(page);
      setOffset((page - 1) * limit);
    }
  }

  function openBookDetail(book: Book) {
    setSelectedBook(book);
  }

  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-2xl font-bold flex items-center gap-2 text-gray-800">
            Tabla virtual
          </h1>
          <p className="text-sm mx-1">
            Tabla interactiva con paginación, filtrado avanzado y backend
            optimizado con SQL, FastAPI y Python, integrada con una interfaz
            dinámica en React.
          </p>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex flex-col sm:flex-row justify-between items-center mb-6  ">
            <div className="flex items-center gap-4">
              <Button
                variant="outline"
                size="sm"
                disabled={page <= 1}
                onClick={() => PageDown()}
              >
                <ChevronLeft className="h-4 w-4 mr-1" /> Anterior
              </Button>
              <div className="flex items-center gap-2">
                <Input
                  type="number"
                  value={page}
                  onChange={(e) => ManualPage(Number(e.target.value))}
                  className="w-16 text-center"
                  min={1}
                  max={Math.ceil(count / limit)}
                />
                <span className="text-sm text-gray-600">
                  de {Math.ceil(count / limit)}
                </span>
              </div>
              <Button
                variant="outline"
                size="sm"
                disabled={page >= Math.ceil(count / limit)}
                onClick={() => PageUp()}
              >
                Siguiente <ChevronRight className="h-4 w-4 ml-1" />
              </Button>
            </div>
            <div className="w-auto mx-5 my-5 ">
              <Input
                onChange={(e) => setSearch(e.target.value)}
                className="border-gray-500"
                type="text"
                placeholder="Buscar por nombre 🔎"
              ></Input>
            </div>
            <div className="flex items-center gap-4">
              <span className="text-sm text-gray-600">
                Total de libros: {count}
              </span>
              <div className="flex items-center gap-2">
                <label htmlFor="limit" className="text-sm text-gray-600">
                  Libros por página:
                </label>
                <Input
                  id="limit"
                  type="number"
                  value={limit}
                  onChange={(e) => setLimit(Number(e.target.value))}
                  className="w-16 text-center"
                  min={1}
                  max={50}
                />
              </div>
            </div>
          </div>

          <div className="rounded-lg border shadow-sm overflow-hidden">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="font-semibold">
                    <TooltipProvider>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() =>
                              setFilter((prev) => ({
                                ...prev,
                                name: !prev.name,
                              }))
                            }
                          >
                            Nombre
                            {filter.name ? (
                              <ChevronDown className="ml-1 h-4 w-4" />
                            ) : (
                              <ChevronUp className="ml-1 h-4 w-4" />
                            )}
                          </Button>
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Ordenar por nombre</p>
                        </TooltipContent>
                      </Tooltip>
                    </TooltipProvider>
                  </TableHead>
                  <TableHead className="font-semibold">
                    <TooltipProvider>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() =>
                              setFilter((prev) => ({...prev, age: !prev.age}))
                            }
                          >
                            Año
                            {filter.age ? (
                              <ChevronDown className="ml-1 h-4 w-4" />
                            ) : (
                              <ChevronUp className="ml-1 h-4 w-4" />
                            )}
                          </Button>
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Ordenar por año</p>
                        </TooltipContent>
                      </Tooltip>
                    </TooltipProvider>
                  </TableHead>
                  <TableHead className="font-semibold">
                    <TooltipProvider>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() =>
                              setFilter((prev) => ({
                                ...prev,
                                author: !prev.author,
                              }))
                            }
                          >
                            Autor
                            {filter.author ? (
                              <ChevronDown className="ml-1 h-4 w-4" />
                            ) : (
                              <ChevronUp className="ml-1 h-4 w-4" />
                            )}
                          </Button>
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Ordenar por autor</p>
                        </TooltipContent>
                      </Tooltip>
                    </TooltipProvider>
                  </TableHead>
                  <TableHead className="font-semibold">
                    <TooltipProvider>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() =>
                              setFilter((prev) => ({
                                ...prev,
                                isbn: !prev.isbn,
                              }))
                            }
                          >
                            ISBN
                            {filter.isbn ? (
                              <ChevronDown className="ml-1 h-4 w-4" />
                            ) : (
                              <ChevronUp className="ml-1 h-4 w-4" />
                            )}
                          </Button>
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Ordenar por ISBN</p>
                        </TooltipContent>
                      </Tooltip>
                    </TooltipProvider>
                  </TableHead>
                  <TableHead className="font-semibold">Estado</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {isLoading ? (
                  Array.from({length: limit}).map((_, index) => (
                    <TableRow key={index}>
                      <TableCell>
                        <div className="h-4 bg-gray-200 rounded dark:bg-gray-700 w-3/4 animate-pulse"></div>
                      </TableCell>
                      <TableCell>
                        <div className="h-4 bg-gray-200 rounded dark:bg-gray-700 w-1/4 animate-pulse"></div>
                      </TableCell>
                      <TableCell>
                        <div className="h-4 bg-gray-200 rounded dark:bg-gray-700 w-1/2 animate-pulse"></div>
                      </TableCell>
                      <TableCell>
                        <div className="h-4 bg-gray-200 rounded dark:bg-gray-700 w-1/3 animate-pulse"></div>
                      </TableCell>
                      <TableCell>
                        <div className="h-4 bg-gray-200 rounded dark:bg-gray-700 w-1/4 animate-pulse"></div>
                      </TableCell>
                    </TableRow>
                  ))
                ) : data.length > 0 ? (
                  data.map((book, index) => (
                    <TableRow
                      key={index}
                      className="cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800"
                      onClick={() => openBookDetail(book)}
                    >
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
                  <TableRow>
                    <TableCell colSpan={5} className="text-center py-4">
                      No se encontraron libros
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </div>
        </div>
      </main>
      {selectedBook && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg max-w-lg w-full">
            <h2 className="text-2xl font-bold mb-4">{selectedBook.name}</h2>
            <p>
              <strong>Autor:</strong> {selectedBook.author}
            </p>
            <p>
              <strong>Año:</strong> {selectedBook.age}
            </p>
            <p>
              <strong>ISBN:</strong> {selectedBook.isbn}
            </p>
            <Button className="mt-4" onClick={() => setSelectedBook(null)}>
              Cerrar
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
