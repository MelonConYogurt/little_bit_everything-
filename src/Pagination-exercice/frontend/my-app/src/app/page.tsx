import Link from "next/link";
import {Button} from "@/components/ui/button";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-100 to-white">
      <main className="container mx-auto px-4 py-16">
        <h1 className="text-4xl font-bold text-center mb-6 text-blue-800">
          Bienvenido a Nuestra Librería
        </h1>
        <p className="text-xl text-center mb-8 text-gray-600">
          Descubre un mundo de historias, conocimiento y aventuras en nuestras
          estanterías.
        </p>
        <div className="text-center">
          <Button
            asChild
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            <Link href="/books?page=1">Ver tabla de libros</Link>
          </Button>
        </div>
      </main>
    </div>
  );
}
