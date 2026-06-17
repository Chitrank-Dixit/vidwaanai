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

### Verse 1 (Vishnu Puran 0.11061)
- **Original**: ब्रह्मा आदि सम्पूर्ण देवशण तथा मनुष्य और पशु आदि सभी विष्णुमायारूप महान्‌ आवर्तमें पड़कर मोहरूप अन्धकारसे आयृत हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11062)
- **Original**: हे भगवन्‌ ! [ जन्म और मरणके चक्रमें पड़े हुए ] ये पुरुष जीवके भव-बन्चनको नष्ट करनेवाले आपकी आराधना करके भी जो नाना प्रकास्की कामनाएँ ही माँगते हैं यह आपकी माया ही है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11063)
- **Original**: मैंने भी पुत्रोंकी जयकामनासे शज्ुपक्षको पराजित करनेके लिये ही आपकी आराधना की है, मोक्षके लिये नहीं। यह भी आपकी मायाका ही विल्ास है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11064)
- **Original**: पुण्यहीन पुरुषोंकों जो कल्पवक्षसे भी कौपीन और आच्छादन-बख्वमात्रकी ही कामना होती है यह उनका कर्म-दोष-जन्य अपराध ही है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11065)
- **Original**: है अखिलजगन्माया-मोहकारी अच्यय प्रभो ! आप प्रसन्न होइये और हे भूतेश्वर ! “मैं ज्ञानवान्‌ हुँ" मेंरे इस अज्ञानको नष्ट कीजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11066)
- **Original**: हे चक्रपाणे ! आपको नमस्कार है, हे शार्ज््धर ! आपको नमस्कार है; हे गदाधघर ! आपकव्ये नमस्कार है; हे लंखपाणे ! हे विष्णों ! आपको बारम्जार नमस्कार है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11067)
- **Original**: मैं स्थूल चिह्रोंसे प्रतीत होनेवाले आपके इस रूपको ही देखती हूँ; आपके वास्तविक परस्वरूपको मैं नहीं जानती; हे परमेश्वर ! आप प्रसन्न होइये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11068)
- **Original**: श्रीपराहरजी खोल्के-- अदितिद्वारा इस प्रकार स्तुति किये जानेपर भगवान्‌ विष्णु देवमातासे हैसकर जोले--“हे देखि ! तुम तो हमारी माता हो; तुम्त प्रसन्न होकर हमें वरदायिनी होओ''
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11069)
- **Original**: अदिति बोत्ली--है पुरुषसिंह ! तुम्हारी इच्छा पूर्ण हो। त्रुम मर्त्यलोकमें सम्पूर्ण सुरासुरोंसे अजेय होगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11070)
- **Original**: अआ्रीपराह्रजी बोले--तदनन्तर शक्रपत्री शचीके सहित कृष्णप्रिया सत्यभामाने अदितिको पुनः-पुनः प्रणाम करके कहा--“माता ! आप प्रसन्न होइये'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11071)
- **Original**: अदिति बोली--हे सुन्दर भूकृटिवाल्ी ! मेरी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11072)
- **Original**: 390 श्रीपराशर उवाच अदित्या तु कृतानुज्ञो देवराजो जर्नादनम्‌। यथावत्यूजयामास बहुमानपुरस्सरम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11073)
- **Original**: 28 श्री च सत्यभामायै पारिजातस्य पुष्पकम्‌ । न ददौ मानुषीं मत्वा स्वयं पुष्पैरछल्डृता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11074)
- **Original**: 29 ततो ददर्श कृष्णो5पि सत्यभामासहायवान्‌ । देवोद्यानानि हृद्यानि नन्दनादीनि सत्तम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11075)
- **Original**: 30 दर्दर्श च सुगन्धारय॑ मम्जरीपुझ्रधारिणम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11076)
- **Original**: नित्याह्नादकरं ताप्रबालू्पललवशोभितम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11077)
- **Original**: 31 मथ्यमाने5मृते जाते जातरूपोपमत्वचम्‌। पारिजातं जगन्नाथ: केशवः केशिसूदन:ः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11078)
- **Original**: 32 तुतोष परमप्रीत्या तरुराजमनुत्तमम्‌ । त॑ दृष्ठा प्राह गोविन्द सत्यभामा द्विजोत्तम । कस्मान्न द्वारकामेष नीयते कृष्ण पादपः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11079)
- **Original**: 33 यदि चेत्त्वद्नचः सत्यं त्वमत्यर्थ॑ प्रियेति में । मद्रेहनिष्कुटार्थाय तदरय॑ नीयतां तरु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11080)
- **Original**: 34 न में जाम्बबती तादृगभीष्टा न च रुक्मिणी । सत्ये यथा त्वमित्युक्ते त्वया कृष्णासकृत्रियम्‌
- **Translation**: 

---

