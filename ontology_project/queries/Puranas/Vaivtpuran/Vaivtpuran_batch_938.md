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

### Verse 1 (Vaivtpuran 543.17074)
- **Original**: $%$%ऊ$%ऊऋऊऊक $5%$%$$%%$%%$%%%#$%##%%#%####%#%##%%##5###8#%#%####### 55% $ ग्रीष्मकालीन सूर्यकफे समान चमकौली शक्ति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17075)
- **Original**: बाणको समर्पित कर दिया। तत्पश्चात्‌ बलिने जिस चलायी, किंतु महाबली अर्जुनने उसे भी अनायास
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17076)
- **Original**: वेदोक्त स्तोत्रद्वारा उनकी स्तुति को थी, उसी ही काट गिराया। यह देखकर बाणने पाशुपतास्त्रको,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17077)
- **Original**: स्तोत्रद्वारा चन्द्रशेखरने शक्तियोंके स्वामी जगदी श्वर जिसकी प्रभा सैकड़ों सूर्योके समान थी और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17078)
- **Original**: श्रीकृष्णका स्तवन किया। तब श्रीहरिने बुद्धिमान्‌ जो अत्यन्त भयंकर, अमोघ तथा विश्वका संहार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17079)
- **Original**: बाणको 'मृत्युझ्य' नामक ज्ञान प्रदान किया और करनेबाला था, हाथमें लिया। उसे देखकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17080)
- **Original**: उसके शरीरपर अपना कर-कमल फिराकर उसे चक्रपाणिने अपने भयंकर सुदर्शनचक्रकों चला अजर-अमर बना दिया। दिया। उस चक्रने रणभूमिमें बाणके हजारों. तदनन्तर बाणने बलिकृत स्तोत्रद्वारा भक्तिपूर्वक हाथोंको काट डाला और वह भयंकर पाशुपतास्त्र श्रीहरिका स्तवन किया और उसी देबसमाजमें पहाड़ी सिंहकी तरह भूमिपर गिर पड़ा। तदनन्तर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17081)
- **Original**: रत्ननिर्मित आभूषणोंसे विभूषित अपनी श्रेष्ठ कन्या जो प्रलयकालीन अग्निकी शिखाके समान प्रकाशमान,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17082)
- **Original**: उषाको लाकर भक्तिसहित श्रीकृष्णको प्रदान कर लोकमें दारुण तथा अमोघ है; बह पाशुपतास्त्र
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17083)
- **Original**: दिया। फिर उसने भक्तिपूर्वक कंधे झुकाकर पाँच पशुपति शिवके हाथमें लौट गया। बाणके शरीर-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17084)
- **Original**: लाख गजराज, बीस लाख घोड़े, रत्नाभरणोंसे रक्तसे वहाँ भयंकर नदी बह चली और बाण
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17085)
- **Original**: विभूषित एक हजार दासियाँ, सब कुछ प्रदान चेष्टाहित होकर भूमिपर गिर पड़ा। उस समय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17086)
- **Original**: करनेवाली बछड़ोंसहित एक सहस्र गौएँ, करोड़ों- व्यथाके कारण उसकी चेतना नष्ट हो गयी थी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17087)
- **Original**: करोड़ों मनोहर माणिक्य, मोती, रत्न, श्रेष्ठ मणियाँ तब जगदगुरु भगवान्‌ महादेव वहाँ आये और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17088)
- **Original**: और हीरे तथा हजारों सुवर्णनिर्मित जलपात्र बाणको उठाकर उन्होंने अपनी छातीसे लगा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17089)
- **Original**: एबवं भोजनपात्र श्रीकृष्णकों दहेजमें दिये। नारद! लिया। फिर बाणको लेकर वे वहाँ चले, जहाँ फिर बाणने शंकरजीकी आज्ञासे सभी तरहके भगवान्‌ जनार्दन विराजमान थे। वहाँ पहुँचकर अग्रिशुद्ध श्रेष्ठ महीन वस्त्र तथा ताम्बूल और ; सक्लराफ़्त उसकी सामग्रियोंके विविध प्रकारके हजारों श्रेष्ठ [
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17090)
- **Original**: पूर्णपात्र भक्तिपूर्ण हृदयसे दहेजमें दिये। तत्पश्चात्‌ कन्याको भी श्रीहरिके चरणकमलोंमें समर्पित करके वह ढाह मारकर रो पड़ा। इस प्रकार उसने बह कार्य सम्पन्न किया। तब श्रीकृष्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17091)
- **Original**: बाणको वेदोक्त मधुर वचनोंद्वारा वरदान देकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17092)
- **Original**: शंकरजीकी अनुमतिसे द्वारकापुरीको प्रस्थित हुए। वहाँ पहुँचकर स्वयं श्रोहरिने महात्मा बाणकों ----
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17093)
- **Original**: उस कन्याकों नवोढ़ा (नवविवाहिता वधू) 5: ../:-
- **Translation**: 

---

