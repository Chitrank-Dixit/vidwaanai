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

### Verse 1 (Vaivtpuran 543.14874)
- **Original**: मनको वशमें रखकर वह नित्य-निरन्तर श्रीकृष्णके तथा यौवनके मदसे उन्मत्त हो सदा उदण्डतापूर्ण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14875)
- **Original**: शुभागमनका चिन्तन करता रहा। इधर मधथुरामें बर्ताव किया करता था। महामुने ! श्रीकृष्णने उससे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14876)
- **Original**: सूर्यदेव अस्ताचलको चले गये। तब श्रीकृष्णकी विनयपूर्वक वस्त्र माँगा। उसने वस्त्र तो उन्हें दिया
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14877)
- **Original**: आज्ञा लेकर अक्रूर अपने घरकों गये और नहीं, उलटे कठोर बातें सुनायीं। श्रीकृष्ण भी नन्‍्द एवं बलदेव आदिके साथ आनन्दपूर्वक किसी बैष्णवके घर गये, जो कपड़ा बुननेका व्यवसाय करता था। उसने अपना सर्वस्व भगवान्‌कों समर्पित कर रखा था। उस भक्तने श्रीनिवासको प्रणाम करके उनका पूजन किया और भगवान्‌ने उसको अपना वह दास्यभाव प्रदान किया जो ब्रह्मा आदि देवताओंके लिये भी दुर्लभ है। वहाँ उत्तम मिष्टान्न भोजन करके सब लोग पलंगपर सो गये। तदनन्तर श्रीकृष्ण कुब्जाके घर गे (0.
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14878)
- **Original**: ) पधारे। उसने स्वागत किया। भगवानने उसको *
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14879)
- **Original**: हि प बताया--' प्रिये ! श्रीरमावतारके समय तुमने मेरे . ») 28 भ्
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14880)
- **Original**: लिये तप किया था; अत: अब मुझसे मिलकर हर 00///7 -0 आक-8
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14881)
- **Original**: जरा-मृत्युरहित और अत्यन्त दुर्लभ मेरे परमधाम धोबी बोला--ओ मूढ़! तू गोप-जनोंका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14882)
- **Original**: गोलोकको जाओ।' इसी समय गोलोकसे एक लाडला है। यह वस्त्र गायके चरबाहोंके योग्य
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14883)
- **Original**: रत्ननिर्मित रथ वहाँ आया और कुब्जा दिव्य देह नहीं है; अत्यन्त दुर्लभ और राजाओंके ही
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14884)
- **Original**: धारण करके उसीके द्वारा गोलोककों चली गयी। उपयोगमें आने योग्य है। मुने! वह वहीँ चन्द्रमुखो गोपी हो गयी और धोबीकी यह बात सुनकर मधुसूदन हँसे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14885)
- **Original**: कितनी ही गोपियाँ उसकी परिचारिका हुईं। बलदेव, अक्रूर और गोपगण भी हँसने लगे।। भगवान्‌ नन्दनन्दन भी क्षणभर कुब्जाके यहाँ श्रीकृष्णे एक ही तमाचेमें उस धोबीका काम
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14886)
- **Original**: ठहरकर पुन: अपने निवास-मन्दिरमें लौट आये, तमाम करके कपड़ोंका वह गट्टर ले लिया और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14887)
- **Original**: जहाँ ननन्‍्दजी सानन्द विराजमान थे। उधर भयविह्नल सखाओंसहित उन्होंने अपनी रुचिके अनुसार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14888)
- **Original**: कंसने रातकों नींद आ जानेपर दुःखद दुःस्वप्र वस्त्र धारण किये। वह रजकराज (धोबियोंका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14889)
- **Original**: देखा, जो उसकी मृत्युका सूचक था। उसने देखा, सरदार) दिव्य देह धारण करके श्रीकृष्ण-पार्षदोंसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14890)
- **Original**: सूरज आकाशसे गिरकर पृथ्वीपर पड़ा है और वेष्टित रत्रमय विमानद्वारा गोलोककों चला गया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14891)
- **Original**: उसके चार खण्ड हो गये हैं। मुने! इसी तरह उसका वह दिव्य शरीर अक्षय यौवनसे युक्त, जरा चन्द्रमण्डल भी आकाशसे भूमिपर गिरकर दस और मृत्युका निवारक, श्रेष्ठ पीताम्बरसे सुशोभित,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14892)
- **Original**: खण्डोंमें विभक्त दिखायी दिया। उसने कुछ ऐसे मन्द मुस्कानसे विलसित, श्यामकान्तिसे कमनौय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14893)
- **Original**: पुरुष देखे, जिनकी आकृति विकृत थी। वे और मनोहर था। गोलोकमें पहुँचकर वह भी
- **Translation**: 

---

