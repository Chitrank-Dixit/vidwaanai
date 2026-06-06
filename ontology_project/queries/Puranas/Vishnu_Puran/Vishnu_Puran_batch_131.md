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

### Verse 1 (Vishnu Puran 0.2601)
- **Original**: भ्रपणशील ग्राहगण और तरलतरंगोंसे पूर्ण सम्पूर्ण महासागर क्षुब्ध हो गया, तथा पर्वत और बनोपबनोंसे पूर्ण समस्त पृथिबरी हिलने लगी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2602)
- **Original**: तथा महामति प्रह्मादजों अपने ऊपर दैल्योंद्रास लादे गये उस्र सम्पूर्ण पर्वत-समूहको दूर फेंककर जलरूसे बाहर निकल आये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2603)
- **Original**: तब आकाशादिरूप जगत्क्वे फिर देखकर उन्हें चित्तगें यह पुनः भान हुआ कि मैं अह्लाद हूँ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2604)
- **Original**: और उन महाबुद्धिमानने मत, खाणी और हारीरके संयमपूर्वक चैर्य घारणकर एक़ाग्र-चित्तसे पुनः भगवान्‌ _अनादि पुरुषोत्तमकी स्तुति की
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2605)
- **Original**: अद्भादजी कहने लगे--हे परमार्थ ! हे आर्थ (दुइ्यरूप) ! हे स्थूलसूक्ष्म (जाग्रतू-स्वप्रदृश्य- स्वरूप) ! हे क्षराक्षर (कार्य-कारणरूप) हे व्यक्ताव्यक्त (दृश्यादृश््यस्वक्ूप) ! है कल्म्नतीत ! हे सकलेश्वर ! हे निरज्ञन देव ! आपको नमस्कार है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2606)
- **Original**: हे गुणोंकों अनुरज्ञित करनेवाले ! हे गुणाधार ! हे निर्गुणात्मन्‌ ! हे गुणस्थित ! हे सूर्त और अमूर्तरूप महामूर्तिमन्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2607)
- **Original**: हे सुक्ष्ममूर्ते ! हे प्रकाशाप्रकाशस्वरूप ! [ आपको नमस्कल है]
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2608)
- **Original**: हे विकयक और सुन्दररूप ! हे विद्या और अविद्यामय अच्यृत ! है सदसत्‌ (कार्यकारण) रूप जगत्‌के डद्धलस्थान और सदसज्जगतके पाऊुक ! [ आपको नमस्कार है]
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2609)
- **Original**: हे नित्यानित्य (आकाहझघटादिरूप) प्रपश्ञात्मन्‌ ! हे प्रपश्लसे पृथक रहनेवाले हे ज्ञानियोंके आश्रयरूप ! है एकानेकरूप आदिकारण वासुदेख ! [ आपको नमस्कार है ]
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2610)
- **Original**: जो स्थुल-सूक्ष्मरूप और स्फुट-प्रकाशमय हैं, जो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2611)
- **Original**: 94 विश्व “यतशैतदबविश्वहेतो- श्रीविष्णुपुराण [ अ0 20 अधिष्ठानरूपसे सर्वभूतस्वरूप तथापि जस्तुत: सम्पूर्ण अप्रोज्स्तु तस्मे पुरुषोत्तमाय
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2612)
- **Original**: भूतादिसे परे हैं, विश्वक कारण न होनेपर भी जिनसे यह श्रीपएद्ार उताच आविर्भूव भगवान्‌ पीताम्बरधरों हरिः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2613)
- **Original**: 14 ससम्भ्रमस्तमात्मेक्य समुत्यायाकुलाक्षरम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2614)
- **Original**: नमोस्तु विष्णवेत्येतद्‌ व्याजहारासकृद्‌ द्विज
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2615)
- **Original**: 15 अक्वाद उवाच देव प्रपन्नार््तिर प्रसादं कुरू केशव। अवलोकनदानेन भूयो मां पावयाच्युत
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2616)
- **Original**: 16 अ्रीपगवानुकाच कुर्वतस्ते प्रसन्नोडह भक्तिमव्यभिच्नारिणीम्‌ । यथाभिलघितो मत्त: प्रह्लाद ब्रियतां वर:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2617)
- **Original**: 17 नाथ योनिसहस््रेषु चेषु येष व्जाम्यहम्‌ । तेषु तेघ्च्युताभक्तिरच्युतास्तु सदा त्वयि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2618)
- **Original**: 18 मयि भक्तिस्तवास्व्येव भूयो5प्येयं॑ भविष्यति। बरस्तु मत्त: प्रह्लाद बश्रियतां यस्तवेप्सित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2619)
- **Original**: 20 प्रह्मद उवाच म्रथ्ि द्वेषानुबन्धो5भूस्संस्तुतावुद्यते तब । मत्पितुस्तत्कृतं पापं देख तस्य ग्रणइ्यतु
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2620)
- **Original**: 29 शस्त्राणि पातितान्यड्रे क्षिप्तो यक्चाअिसंहतौ । दंशितओरणैर्दत्त॑ यद्विष॑ मप्र भोजने
- **Translation**: 

---

