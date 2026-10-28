export function PageNotFound() {
  return (
    <div className="flex flex-col items-center justify-center">
      <h1 className="text-4xl font-bold text-white">Erreur 404</h1>
      <p className="mt-4 text-lg text-gray-300">
        La page que vous recherchez n'existe pas.
      </p>
    </div>
  );
}

export default PageNotFound;  