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

### Verse 1 (Vaivtpuran 18.1359)
- **Original**: जब फिर वह उनका दर्शन न कर सका तब
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1360)
- **Original**: शोकसे पीड़ित हो गया। ध्यानगत बालकको पुनः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1361)
- **Original**: न देखनेपर बह गोपीकुमार पीपलकी जड़पर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1362)
- **Original**: बैठकर रोने लगा। तब उस रोते हुए बालककों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1363)
- **Original**: सम्बोधित करके आकाशवाणी हुई। आकाशबाणीका कथन सत्य, प्रबोधयुक्त, हितकर एवं संक्षिप्त था।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1364)
- **Original**: आकाशवाणी बोली--' बालक ! एक बार जो रूप
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1365)
- **Original**: तेरे दृष्टिपथमें आ चुका है, वही इस समय पर्याप्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1366)
- **Original**: + ब्रह्मरवणए्ड + 65 5$5#$$ 5 #$ # 5 % $ $ # 5 $ # $ $ 5 $ $ $ $ 5 5 $ $ #$ 55 % 5 554 # $ 5 # 1 5 5 % 4 ऋ 55% छ 54% 5 4 5 5 55 # 5 8 8 है। अब फिर तुझे उसका दर्शन नहीं हो सकता;
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1367)
- **Original**: अन्त होनेपर जब तुझे दिव्य शरीर प्राप्त होगा, तब क्योंकि जिनके अन्तःकरणकी वासना परिपक्क
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1368)
- **Original**: तू पुनः जन्म, मृत्यु और जराका नाश करनेवाले 7। ।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1369)
- **Original**: गोबिन्दका दर्शन करेगा। यह सुनकर वह बालक बड़ी प्रसन्नताके साथ पुनः ध्यानके प्रयाससे विरत हो गया। उसने समय आनेपर मन-ही-मन श्रीकृष्णका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1370)
- **Original**: त्याग दिया। उस समय स्वर्गलोकमें दुन्दुभियाँ बजने लगीं। आकाशसे पृथ्वीपर फूलोंकी वर्षा होने लगी। इस प्रकार महामुनि नारद शापमुक्त हो गये। गोप-शरीरका त्याग करके वह जीव ब्रह्म-विग्रहमें विलीन हो गया। वह नित्यस्वरूप तो है हो, पूर्वकालमें उसका आविर्भाव हुआ और भिन्न कालमें वह तिरोहित हो गया। नित्यरूपधारी जो भक्तजन हैं, उनका अपनी ् 5 हे इच्छासे आविर्भाव अथवा तिरोभाव होता है। नहीं हुई है, ऐसे कुयोगियोंको उस स्वरूपका [उन्हें जन्म, मृत्यु, जरा और व्याधिका स्पर्श दर्शन होना अत्यन्त कठिन है। तेरे इस शरीरका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1371)
- **Original**: नहीं होता। (अध्याय 20-21) हजल+> अन्य... >> ब्रह्माजीके पुत्रोंके नामोंकी व्युत्पत्ति सौति कहते हैं--शौनकजी! तदनन्तर कुछ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1372)
- **Original**: प्रकट हुआ, वह “मरीचि' कहलाया। जिस कल्प व्यतीत होनेपर जब ब्रह्माजी पुनः सृष्टि-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1373)
- **Original**: बालकने जन्मान्तरमें क्रतुसंघ (यज्ञसमूह)-का कार्यमें संलग्न हुए, तब उनके 'नरद' नामक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1374)
- **Original**: सम्पादन किया था, वह वर्तमान जन्ममें ब्रह्माजीका कण्ठदेशसे मरीचि आदि मुनियोंके साथ वे।पुत्र होनेपर भी उसी क्रतुके नामपर “क्रतु' शापमुक्त मुनि प्रकट हुए। इसी कारणसे उन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1375)
- **Original**: कहलाया। ब्रह्माजीका मुख प्रधान अद्भ है। उस मुनीन्द्रकी 'नारद' नामसे ख्याति हुई। ब्रह्माजीका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1376)
- **Original**: अड्गभसे उत्पन्न हुआ बालक इर अर्थात्‌ तेजस्वी जो पुत्र उनके चेतस्‌ (चित्त)-से प्रकट हुआ,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1377)
- **Original**: था, इसलिये “अड्लिरा' नामसे प्रसिद्ध हुआ। उसका नाम उन्होंने 'प्रचेता' रखा। जो उनके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1378)
- **Original**: शौनक! भृगु शब्द अत्यन्त तेजस्वीके अर्थमें दक्षिण पार्श्ले सहसा उत्पन्न हुआ, वह सब
- **Translation**: 

---

