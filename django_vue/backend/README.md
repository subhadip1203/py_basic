## Developments
Setup Virtual Environment in the project directory :
  1. Create Virtual environment : `python3 -m venv env`
  2. starting Virtual environment : `source env/bin/activate`
  3. stopping Virtual environment : `deactivate`

2. Setup and install Django dependencies
  - for new project install django python-dotenv gunicorn etc 
  `pip install django gunicorn  python-dotenv`

  - to save installed packages :
  `pip freeze > requirements. txt`

  - to install packages from requirements. txt file :
  `pip install -r requirements.txt `


3. Environment Variables: make a file `.env`.

4. Local API Server uses a self signed certificate

  - create a folder with name cert:  `mkdir cert`
  - go inside the folder : `cd cert`
  - as django & gunicorn user 127.0.0.1 as host , create a host in the name of 127.0.0.1  `mkcert -cert-file cert.pem -key-file key.pem  127.0.0.1`
  - install the cert in the laptop or system `mkcert -install`


5. Run the server by gunicorn 

  - without ssl certificates : `gunicorn project_setup.wsgi:application --bind 0.0.0.0:8000`
  - with ssl certificates : `gunicorn project_setup.wsgi:application --keyfile=./cert/key.pem --certfile=./cert/cert.pem`
  - with certificate and hot reload : `gunicorn project_setup.wsgi:application --reload --keyfile=./cert/key.pem --certfile=./cert/cert.pem`

6. Use Scripts from `package.json` to run the build

<br/>

## CodePush Scripts

```sh
# Codepush deployments
appcenter codepush deployment list -a novelship/Novelship.Android -k

# Codepush release
appcenter codepush release-react -a novelship/Novelship.iOS --plist-file "ios/novelship/Info.plist" -d Staging

```

## React & Components

### How to work on a new Component?

Start by creating your component in `app/component`.

- Components must not include their own paddings, margin, shadow, border and position unless they will be always used with those styles. For better reusability, components must not define how their environment is. We can always easily wrap them in a `<Box>` and add the required wrapping styles.
- If the component is going to be used at too many places with multiple conditions. Duplicate it, don't abstract more. [Read more...](https://medium.com/better-programming/when-dry-doesnt-work-go-wet-6befda0444bf)

<br/>

## Styling

- See [Restyle By Shopify](https://github.com/Shopify/restyle)
- Provides support for theming, typography and responsive UI. Inspired by the popular [Styled System Library](https://styled-system.com/)
- Use predefined colors from `app/styles/theme.ts`
- Follow Font & Spacing from `app/styles/theme.ts`
- Font Used is **IBM Plex Sans**. All components must use these fonts
- Do not use fontWeight Property. Use fontFamily with one of the options from `app/styles/theme.ts.Fonts`. Using only fontWeigh will apply the weight on a wrong font.
- Ensure to disable fontscaling when directly using a third party or react native component which directly displays text. We will support fontscaling when we setup responsive font sizes on the app.

<br/>

## UI State Management

- Manage local component state with `React.useState`
- Global State : [Easy Peasy (Redux Wrapper)](https://easy-peasy.now.sh/)
- Import state hooks from `app/store/` only. These have been types setup.

<br/>

## Server State Management

- Query API using React Query.
- React Query has built in hooks for data fetching, caching, mutations, suspense and much more. Read the [docs](https://react-query.tanstack.com/overview) for more info.

<br/>

## API & Data Fetching

1. `common/api`: Exposes API with all `fetch`, `post`, `put`, `patch` and `remove` methods.
   1. API.fetch takes in the params for filtering, sorting, joining etc as per Backend API specs.
   2. API.fetch also works for external APIs.

<br/>

## Type Checking

- Project is ready to use typescript.
  - [Typescript Docs](https://www.typescriptlang.org/docs/handbook/basic-types.html)
  - [Typescript React Cheatsheet](https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/basic_type_example)

<br/>

## File Structure

- `/app/components`: base reusable components
- `/app/config`: base configurations
- `/app/hooks`: app hooks or native only hooks
- `/app/navigation`: Navigation routes and stacks
- `/app/services`: services/integrations, like `utils` but are non functional
- `/app/store`: Global state store and controllers
- `/app/styles`: base style configs
- `assets/`: Assets to be bundled with app
- `/common/api`: api utils
- `/common/constants`: constants
- `/common/utils`: basic utils, mostly pure functional
- `/types`: common type definitions

<br/>

## Assets

- Image assets must be stored in AWS S3 and proxied with Imgix. If the asset is used appwide or on main components like splash, store it in `/assets`
- Use `auto=format,compress` for all imgix image query. `compress` can be dropped for some cases
- Display responsive images: [Imgix React Native Guide](https://support.imgix.com/hc/en-us/articles/360039259332-Using-imgix-in-React-Native?mobile_site=true)
- Create React Native SVGs [React SVGR](https://react-svgr.com/playground/?native=true&typescript=true)
  <br/>

## Code Standards

- Prettier + Eslint
- Auto Prettify on commit

<br/>

## Notes

- Currency Utils Usage:
  - Use `useCurrencyUtils` Hook when using Currency Utils inside React Components.
  - Use `utils/currency` functions elsewhere.
  - By default it uses `currentCurrency` as currency

<br/>

## Architecture

| Level | Name                        | Phase    | Tool     | Why                                           | For      |
| ----- | --------------------------- | -------- | -------- | --------------------------------------------- | -------- |
| 1     | OTA updates                 | To setup | Expo     | Quick OTA Updates                             | All      |
| 2     | Performance and Crashlytics | To setup | Firebase | Tracking performance, crashes and live errors | SRE Team |

<br/>

## Others

- Install recommended Code editor [extensions](./.vscode/extensions.json)
- Only use NPM and not Yarn to manage packages.

<br/>
