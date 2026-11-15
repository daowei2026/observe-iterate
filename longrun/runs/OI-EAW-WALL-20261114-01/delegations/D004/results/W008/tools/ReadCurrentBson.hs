{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE NoOverloadedLists #-}
module ReadCurrentBson where
import Data.Aeson (object, (.=), encode)
import qualified Data.ByteString.Lazy.Char8 as BL
import Frp.Apt.Bson (ToBSON(toBSON), FromBSON(fromBSON))
import Frp.Instance.ISL.Eaw.P1.Products
import Frp.Instance.ISL.Eaw.P1.WallLifecycle
import Frp.Instance.ISL.Eaw.P1.Publication ()
import qualified Main as Obs
import Control.Exception (try, evaluate, SomeException)
main :: IO ()
main = do
 let rows=[Obs.wallStart, Obs.updateA, Obs.updateB, Obs.ended]
 mapM_ (\o -> do
    let doc=toBSON o
    outcome <- try (evaluate ((fromBSON doc :: Maybe WallLifecycleOccurrence)==Just o)) :: IO (Either SomeException Bool)
    case outcome of
     Left err -> BL.putStrLn (encode (object ["occurrence_show" .= show o,"outcome" .= ("EXCEPTION"::String),"exception" .= show err]))
     Right same -> BL.putStrLn (encode (object ["occurrence_show" .= show o,"bson_document_show" .= show doc,"readback_equal" .= same,
       "reader_scope" .= ("existing Publication ToBSON/FromBSON in-memory canonical occurrence; not native physical DBA reader"::String)]))) rows
