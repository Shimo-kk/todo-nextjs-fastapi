export default function NotFound() {
  return (
    <div className="bg-white dark:bg-gray-900 py-6 sm:py-8 lg:py-12">
      <div className="mx-auto max-w-screen-2xl px-4 md:px-8">
        <div className="flex flex-col items-center">
          <p className="mb-4 text-sm font-semibold text-indigo-600 md:text-base">
            404 error
          </p>
          <h1 className="mb-2 text-center text-2xl font-bold text-gray-900 dark:text-white md:text-3xl">
            Page not found
          </h1>

          <p className="mb-12 max-w-screen-md text-center text-gray-500 md:text-lg">
            お探しのページは存在しません。
          </p>

          <a
            href="/"
            className="inline-block rounded-lg bg-indigo-600 dark: px-4 py-2 text-center text-sm font-semibold text-white outline-none ring-indigo-300 transition duration-100 hover:bg-indigo-500 focus-visible:ring active:bg-indigo-300"
          >
            トップへ
          </a>
        </div>
      </div>
    </div>
  );
}
