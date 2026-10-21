import { Outlet, NavLink } from "react-router-dom";

const Layout = () => {
  return (
    <div>
      <nav className="mb-8 flex gap-4 text-slate-50">
        <NavLink
          to="/"
          className={({ isActive }) => (isActive ? "font-bold" : "")}
        >
          Home
        </NavLink>
        <NavLink
          to="/Liste"
          className={({ isActive }) => (isActive ? "font-bold" : "")}
        >
            Liste
        </NavLink>
      </nav>
      <Outlet />
      <footer className="mt-8 text-center text-sm text-slate-500">
        &copy; {new Date().getFullYear()} GameVerse. Tous droits réservés.
      </footer>
    </div>
  );
};

export default Layout;