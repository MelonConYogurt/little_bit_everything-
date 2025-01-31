"use client";

import {useState, useEffect} from "react";
import {useSearchParams} from "next/navigation";
import {useRouter} from "next/navigation";
import {Filter, getDataBooks, type Book} from "@/utils/get";
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
  const searchParams = useSearchParams();
  const router = useRouter();

  const [data, setData] = useState<Book[]>([]);
  const [count, setCount] = useState(0);
  const [limit, setLimit] = useState(
    searchParams.get("limit") !== null ? Number(searchParams.get("limit")) : 10
  );
  const [offset, setOffset] = useState(0);
  const [page, setPage] = useState(
    searchParams.get("page") !== null ? Number(searchParams.get("page")) : 1
  );
  const [isLoading, setIsLoading] = useState(true);
  const [search, setSearch] = useState(
    searchParams.get("search") !== null
      ? String(searchParams.get("search"))
      : ""
  );
  const [filter, setFilter] = useState<Filter>({
    name:
      searchParams.get("name") !== null
        ? Boolean(searchParams.get("name"))
        : null,
    age:
      searchParams.get("age") !== null
        ? Boolean(searchParams.get("age"))
        : null,
    author:
      searchParams.get("author") !== null
        ? Boolean(searchParams.get("author"))
        : null,
    isbn:
      searchParams.get("isbn") !== null
        ? Boolean(searchParams.get("isbn"))
        : null,
  });

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
      router.push(`?page=${newPage}`);
      return newPage;
    });
  }

  function PageDown() {
    setPage((prev) => {
      const newPage = prev - 1;
      setOffset((newPage - 1) * limit);
      router.push(`?page=${newPage}`);
      return newPage;
    });
  }

  function ManualPage(page: number) {
    if (page > 0 && page <= Math.ceil(count / limit)) {
      setPage(page);
      setOffset((page - 1) * limit);
    }
  }

  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold flex items-center gap-2 text-gray-800">
            <BookOpen className="h-8 w-8 text-blue-600" />
            Biblioteca Moderna
          </h1>
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
            <div className="w-40 mx-10 my-5 ">
              <Input
                onChange={(e) => {
                  setSearch(e.target.value);
                  router.push(`search=${e.target.value}`);
                }}
                className="border-gray-500"
                type="text"
                value={search}
                placeholder="Search by name 🔎"
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
                  <TableRow>
                    <TableCell colSpan={5} className="text-center py-4">
                      <div className="flex items-center justify-center p-10 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                        <div role="status">
                          <svg
                            aria-hidden="true"
                            className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                            viewBox="0 0 100 101"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <path
                              d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                              fill="currentColor"
                            />
                            <path
                              d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                              fill="currentFill"
                            />
                          </svg>
                          <span className="sr-only">Loading...</span>
                        </div>
                      </div>
                    </TableCell>
                  </TableRow>
                ) : data.length > 0 ? (
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
    </div>
  );
}
