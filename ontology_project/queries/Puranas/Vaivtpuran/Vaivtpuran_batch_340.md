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

### Verse 1 (Vaivtpuran 16.3294)
- **Original**: श्रीहरिने शंकरको त्रिशूल सौंप दिया। त्रिशूल जाओगे ?' तब मैंने उन रधाकों समझाया और लेकर रुद्र और ब्रह्मा सब देवताओंके साथ कहा--' सभी धैर्य रखें, यह सुदामा आधे क्षणमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3295)
- **Original**: भारतवर्षकों चल दिये। (अध्याय 16) #10 0010 कसेकमिये4050-+>
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3296)
- **Original**: पुष्पदन्तका दूत परकर शहद के शड्डुचूड़के पास जाना और शद्डचूड़के द्वारा प्रति ज्ञानोपदेश भगवान्‌ नारायण कहते हैं--नारद ! तदनन्तर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3297)
- **Original**: कठिन था, परंतु हितैषी व्यक्ति बड़ी सुगमतासे ब्रह्मा दानवके संहार-कार्यमें शंकरको नियुक्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3298)
- **Original**: उसमें जा सकते थे। अत्यन्त उच्च, गगनस्पर्शी करके स्वय॑ उसी क्षण अपने स्थानपर चले गये।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3299)
- **Original**: मणिमय प्राचीरोंसे वह भवन घिरा हुआ था। देवता भी अपने-अपने स्थानोंकों चले गये। तब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3300)
- **Original**: बारह द्वारोंसे भवनकी बड़ी शोभा हो रही थी। चन्द्रभागा नदीके तटपर एक मनोहर बट-वृक्षके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3301)
- **Original**: प्रत्येक द्वारपर द्वारपाल थे। सर्वोत्तम मणियोंद्वारा नीचे जाकर देवताओंका अभ्युदय करनेके विचारसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3302)
- **Original**: निर्मित लाखों मन्दिर, बहुत-से सोपान तथा महादेवजीने आसन जमा लिया। गन्धर्वराज
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3303)
- **Original**: [रत्नमय खंभे थे। एक द्वारको देखनेके बाद पुष्पदन्त शंकरका बड़ा प्रेमी था। उन्होंने उसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3304)
- **Original**: पुष्पदन्तने दूसरे प्रधान द्वारकों भी देखा। उस दूत बनाकर तुरंत हर्षपूर्वक शद्भुचूड़के पास भेजा।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3305)
- **Original**: ट्वारपर हाथमें त्रिशूल लिये एक पुरुष विराजमान उनकी आज्ञा पाकर पुष्पदन्त उसी क्षण शद्भुचूड़के
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3306)
- **Original**: था। उसके मुखपर हँसी छायी थी। उसकी पीली नगरकी ओर चल दिया। दानबराजको पुरी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3307)
- **Original**: आँखें थीं। उसके शरीरका रंग ताँबेके सदूश लाल अमरावतीसे भी श्रेष्ठ थी। कुबेरका भवन उसके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3308)
- **Original**: था। भय उत्पन्न करनेवाले उस द्वारपालसे आज्ञा सामने तुच्छ था। उस नगरकी लम्बाई दस योजन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3309)
- **Original**: पाकर पुष्पदनन्‍्त आगे बढ़ा और दूसरे द्वारकों थी और चौड़ाई पाँच योजन। स्फटिक-मणिके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3310)
- **Original**: लाँघधकर भीतर चला गया। यह दूत युद्धकी सूचना समान रत्रोंसे बने हुए परकोटोंद्वारा वह घिरा था।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3311)
- **Original**: पहुँचानेबाला है--यह सुनकर कोई भी उसे सात दुर्गम खाइयोंसे बह सुरक्षित था। प्रज्वलित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3312)
- **Original**: रोकता नहीं था। इस तरह नौ द्वारोंको लाँघकर अग्रिके समान निरन्तर चमकनेवाले करोड़ों
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3313)
- **Original**: पुष्पदन्त सबसे भीतरके द्वारपर पहुँच गया। वहाँ र्रोंद्वारा उसका निर्माण किया गया था। उसमें
- **Translation**: 

---

