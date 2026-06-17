# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Bramha 0.3121)
- **Original**: उठते थे। उसकी स्त्री और पुत्र भी उसी भगवान्‌ गद्जालोतमें आये और रक्तसे लथपथ हुए
- **Translation**: 

---

### Verse 2 (Bramha 0.3122)
- **Original**: स्वभावके थे। एक दिन अपनी पत्नीको प्रेरणासे अपने अज्जोंको गड्गाजीके जलसे घोया। उस
- **Translation**: 

---

### Verse 3 (Bramha 0.3123)
- **Original**: बह घने जड्ललमें घुस गया। वहाँ उस पापीने स्थानपर वाराह नामक कुण्ड हो गया। इसके बाद
- **Translation**: 

---

### Verse 4 (Bramha 0.3124)
- **Original**: अनेक प्रकारके मृ्ों और पक्षियोंका वध किया। भगवानूने मुँहमें रखे हुए महायज्ञकों दे दिया। इस
- **Translation**: 

---

### Verse 5 (Bramha 0.3125)
- **Original**: कितनॉकों जोवित ही पकड़कर पिंजड़ेमें डाल प्रकार उनके मुखसे यज्ञका प्रादुर्भाव हुआ, इसलिये
- **Translation**: 

---

### Verse 6 (Bramha 0.3126)
- **Original**: दिया। इस प्रकार बहुत दूरतक थूम-फिरकर वह याराहतीर्थ परम पवित्र और सम्पूर्ण अभिलषित
- **Translation**: 

---

### Verse 7 (Bramha 0.3127)
- **Original**: अपने घरकी ओर लौटा। तौसरे पहरका समय बस्तुओंको देनेवाला है। वहाँ किया हुआ ख्रान
- **Translation**: 

---

### Verse 8 (Bramha 0.3128)
- **Original**: था। चैत्र और वैशाख बीत चुके थे। एक ही और दान सब यज्ञोंका फल देता है। जो पुण्यात्मा
- **Translation**: 

---

### Verse 9 (Bramha 0.3129)
- **Original**: क्षणमें बिजली कौंधने लगी और आकासमें मेघोंकी पुरुष वहाँ रहकर अपने पितरोंका स्मरण करता
- **Translation**: 

---

### Verse 10 (Bramha 0.3130)
- **Original**: घटा छा गयी। हवा चली और पानीके साथ है, उसके पितर सब पापोंसे मुक्त हो स्वर्गमें चले
- **Translation**: 

---

### Verse 11 (Bramha 0.3131)
- **Original**: पत्थरोंकी वर्षा होने लगी। मूसलाधार वर्षा होनेके जाते हैं। त््यम्बकर्में एक कुशाबर्त नामक तीर्थ है,
- **Translation**: 

---

### Verse 12 (Bramha 0.3132)
- **Original**: कारण बड़ी भयंकर अवस्था हो गयी। व्याध राह उसके स्मरणमाजसे मनुष्य कृतार्थ हो जाता है।। चलते-चलते थक गया था। जलकी अधिकताके
- **Translation**: 

---

### Verse 13 (Bramha 0.3133)
- **Original**: » वाराहतीर्थ, कुशाब्त, भीलगड़ा और कपोततीर्थकी महिमा * श्8र फातपासरथा छाप पड से सह था। जल, पल
- **Translation**: 

---

### Verse 14 (Bramha 0.3134)
- **Original**: यहारेवाली' पकयावतं ऋतिक या जे यो न जाने क्‍यों कारण मार्गका ज्ञान नहों हो पाता था। जल, थल । पहनती शारशामपनी आर के जो बे शरमाइ पी आयात अकया जज बजाए दआ 48 (5-00 .#मब 443 जनेर+007-487-4%* मम पता हूँ। मेरे इस शरीरकी स्वामिनी भी वही है। 04 24% पके 9 च" [फल अर्थ, काम और मोक्षकी सिद्धिमें वही सर्वदा नरक स+ह- अल मित्र सहायता कस हैंड प्रकता देखकर! यह आशवासव ै++है'203344-2030 4
- **Translation**: 

---

### Verse 15 (Bramha 0.3135)
- **Original**: हँसतो है और खिन्न जानकर मेरे दुःखोंका निवारण 04 फृ 7 >बै+-2 कम के।' '
- **Translation**: 

---

### Verse 16 (Bramha 0.3136)
- **Original**: जाओ है। सचिन आला देव सेन साख की श+क अरे न हुए
- **Translation**: 

---

### Verse 17 (Bramha 0.3137)
- **Original**: और सदा मेरी आहाके ही पालन संलग्न रहती है। ने थोड़ी हो दृश्य अभीतक आओ मन नम कमर व मच 0> अकेली +-अ जा के देवता, धर्म अथवा अर्थ नहीं जानती। बह उसीकी छायामें आकर बैठ गया। उसके सब वस्त्र
- **Translation**: 

---

### Verse 18 (Bramha 0.3138)
- **Original**: मन्त्र, इनकी अनहो+ नल .-0#-
- **Translation**: 

---

### Verse 19 (Bramha 0.3139)
- **Original**: भीग गये थे। वह इस चिन्तामें पड़ा था कि मेरे
- **Translation**: 

---

### Verse 20 (Bramha 0.3140)
- **Original**: पतिब्रता है। # "मर पर भाारआश +प मन स्त्री-बच्चे जीवित होंगे या नहीं। इसी समय पाता मन्त्र 03: अदा क कर “मा 4-+3% कोण करूँ, कहाँ जाऊँ? मेरा यह घर उसके बिना अपनी स्त्री और पुत्र-पौत्रके साथ रहता था। वह
- **Translation**: 

---

