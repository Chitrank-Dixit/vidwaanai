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

### Verse 1 (Markende Puran 0.2241)
- **Original**: एतड़: कशित सर्वममरारिविच्ेप्ठितम्‌। शरणं द; प्रपला: स्मो वधस्तस्य सिचिन्यताम्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2242)
- **Original**: ऋषि कहते हैं --
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2243)
- **Original**: पूर्वकालमें देषताओं और असुरोमें पूरे सौ जर्षोत्क घोर संग्राम हुआ था। उसमें असुरोंका स्वामी महिषासुर था और देवताओंके नायक इन्द्र थे। उस युक्धमें देबताओंकी सेना महाबली असुरोसे परास्त हों गयी। सम्पूर्ण देवताओंकों जीतकर मह्विषासुर इन्र बंद जैठा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2244)
- **Original**: तत्र पराजित देवता प्रजापति ब्रह्माजीको आगे करके उरा स्थानपर गये, जहाँ भगवान्‌ शंकर और विष्णु त्रिराजमान थे
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2245)
- **Original**: देवताओंने महिषासुरके पराक्रण तथा अपनी पराजयका सथाज्रव्‌ वृत्तान्त उन दोतों देवेश्वरोंसे विस्तारपूर्वक्0 कह सुनाया
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2246)
- **Original**: #54 ये बोलले-' भगवन्‌ ! महिषासुर सूर्य, इन्द्र, अग्नि, वायु, चन्द्रमा, यम, वरुण तथा अन्य देबताओंके भो अधिकार छोनकर स्वय॑ ही सबका अधिश्षाता बना थैटा हैं
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2247)
- **Original**: उस दुशत्मा महिगने समस्त पहिथे5सुराणामश्चिपे टेवानां चर पुरंदरे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2248)
- **Original**: देबताओंको स्वर्गसे तिकाल दिया हैं। अब थे तत्रासुरैरमहावीर्यदेवसैन्यं पराजितम्‌। जित्वा त् सकलानू्‌ देवानिन्द्रो5भून्महिषासुर:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2249)
- **Original**: तत: पराजिता देवा: पद्मवोनिं प्रजापतिम्‌। पुरस्कृत्त गतास्तत्र_ यव्रेशगरुउश्यजी
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2250)
- **Original**: मनुष्योंकी भाँति पृथ्वी 59 विचरते हैं
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2251)
- **Original**: दैत्थॉकी शाह रारी करतूत हमने आपलोगोंसे कह सुनायौ। अब हम आपकी हो शरणमें आये हैं। उसके बधधका कोई उपाय सोचिये
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2252)
- **Original**: + देवताओंके ज्ेजसे देखीका प्रोदुर्भाव और महिषासुरक्ती सेनाका बंध 46644 झझार 8 रुझ4.45 15552 5 2:84: 6654 54445 0» 0कसतऊ/ शेर 5 55464 4, बत्थं निशम्य देवानां वच्चांसि मधुसुदनः। चकार कोप॑ शम्भुक्ष श्रुकुटीकुटिलाननौ
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2253)
- **Original**: त्ततोंअतिकोपपूर्णस्थ चक्रिणो वदनात्तत:। निश्चक्ताम पहत्तेजो ब्रह्मण: शंकरस्थ च्ञ
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2254)
- **Original**: अन्येषां चैव देखानां शक्रादीनां शरीरतः । निर्गति सुपहत्तेजस्तच्यैक्य॑ समगच्छत
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2255)
- **Original**: अतीब तेजस: कूट्ट ज्वलन्तमिव पर्वतम्‌। डद्शुस्ते सुरास्तत्र ज्यालाव्यामदिगन्तरम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2256)
- **Original**: अतुर्ल त़त्र तत्तेज: सर्वदेग्शरीरजम्‌। एूकस्थं तदभूनारी व्याम्नलोकत्रर्य त्विष्ा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2257)
- **Original**: यदभूच्छाम्धर्ब॑ तेजस्तेवाजाबत सन्मुखम्‌। बाम्घेन चाभवन्‌ केशा बाहयों विष्णुतेजसा
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2258)
- **Original**: सौप्येन स्तनयोर्युग्म॑ मध्य॑ चैन्द्रेण चाभवत्‌। सारुणेव क्ष जड्घोरू नितप्बस्तेजसा भुव:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2259)
- **Original**: बरह्मणस्तेजसा पादौ तदहुल्योडर्कतेजसा । बसूनां च कराज्लुल्य: कौष्चेरेण चर नासिका
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2260)
- **Original**: लस्थास्तु दनताः सामभूता; प्राजापत्मेन तेजसा
- **Translation**: 

---

