"use client";

import {useState, useEffect} from "react";
import {getDataBooks, Book} from "@/utils/get";

export default function Table() {
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
    <div className="bg-white flex flex-col justify-center items-center w-96 h-96 p-4">
      <h1 className="text-black text-3xl mb-4">Tabla de Libros</h1>
      {data.length > 0 ? (
        <table className="table-auto border-collapse border border-gray-300 w-full text-sm text-left">
          <thead>
            <tr>
              <th className="border border-gray-300 px-4 py-2">Nombre</th>
              <th className="border border-gray-300 px-4 py-2">Autor</th>
              <th className="border border-gray-300 px-4 py-2">Edad</th>
              <th className="border border-gray-300 px-4 py-2">ISBN</th>
            </tr>
          </thead>
          <tbody>
            {data.map((book, index) => (
              <tr key={index} className="hover:bg-gray-100">
                <td className="border border-gray-300 px-4 py-2">
                  {book.name}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {book.author}
                </td>
                <td className="border border-gray-300 px-4 py-2">{book.age}</td>
                <td className="border border-gray-300 px-4 py-2">
                  {book.isbn}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-gray-500">No hay datos disponibles</p>
      )}
    </div>
  );
}
