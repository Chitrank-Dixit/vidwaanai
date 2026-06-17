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

### Verse 1 (Vishnu Puran 0.361)
- **Original**: 42 सच्त्वोद्रिक्तोइसि भगवन्‌ गोविन्द पृथिवीमिमाम्‌ । समुद्धर भवायेश जझज्नो देद्ाब्जलोचन
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.362)
- **Original**: 43 सर्गप्रवृत्तिभवतोी.._ जगतामुपकारिणी । भ्रव॒त्वेषा नमस्तेउस्तु शन्नो देहाब्जलोचन
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.363)
- **Original**: डड श्रीपराइर उवाच एवं संस्तूयमानस्तु परमात्मा महीधर:। उजहार क्षिति क्षिप्रं न्यस्तवांक्ष महाम्भसि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.364)
- **Original**: 45 तस्पोषरि जलोघस्य महती नौरिव स्थिता । बिततत्वात्तु देहस्य न मही याति सम्म्वम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.365)
- **Original**: 46 तत: क्षिति समां कृत्वा पृथिव्यां सोइचिनोडिरीन्‌ । यथाविभागं॑ भगवाननादि: परमेश्वर:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.366)
- **Original**: 47 प्रावसर्गदग्धानखिलान्पर्वतान्पृधिवीतले । अमोधेन प्रभावेण ससर्जामोघवाज्छित:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.367)
- **Original**: 48 भूविभाग्ग ततः कृत्वा सप्रद्गीपान्यथातथम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.368)
- **Original**: भूराद्यां श्रतुरों लछोकान्यूर्ववत्समकल्पयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.369)
- **Original**: 49 ब्रह्मसपधरो देवस्ततोडइसो रजसा शत: । चकार सुष्टि भगवांभ्तुर्वक्त्रधरों हरि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.370)
- **Original**: 50 निमित्तमात्रमेवाउसो सृज्यानां सर्गकर्मीणि । प्रधानकारणीभूता चतो वै सृज्यशक्तय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.371)
- **Original**: 51 निमित्तमात्रन॑ मुक्त्वैय॑ नान्यत्किल्विदपेक्षते । नीयते तपतां श्रेष्ठ स्वशक्त्या वस्तु खस्तुताम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.372)
- **Original**: 52 हे जगत्पते ! परमार्थ (सत्य बस्तु) तो एकमान्न आप ही हैं. आपके अतिरिक्त और कोई भो नहीं है। यह आपकी ही म्रहिमा (माया) है जिससे यह रूम्पूर्ण चराचर जगत व्याप्त है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.373)
- **Original**: यह जो कुछ भी मूर्तिमान्‌ जगव्‌ दिखायी देता है ज्ञानस्वरूय आपहीका रूप है । अजितेद्धिय लोग भ्रमसे इसे ज़गत्‌-रूए देखते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.374)
- **Original**: इस एप्पूर्ण ज्ञान- स्वरूप जगतको बुद्धिहीन ल्जेग अर्थरूप देखते है, अतः बे निररर मोहमय संसार-सागरमें भटका करते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.375)
- **Original**: है परमेश्वर ! जो लोग शुद्धच्तति और विज्ञानवेत्ता हैं थे इस सम्पूर्ण संसारकों आपका ब्ानात्मक स्वलप ही देखते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.376)
- **Original**: हे सर्व ! हे सर्वात्मन्‌ ! प्रसन्न होइये। हे अप्रमेयात्मन्‌! हे कमलनयन ! संसारके निवासके लिये पृथित्रीका उद्धार करके हमको शान्ति प्रदान कीजिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.377)
- **Original**: है भगवन्‌ ! हे गोविन्द ! इस समय आप सत्त्वप्रधान हैं; अत: हे इंद्ा ! जगतके उद्धातके लिये आप इस पृथिवीका उद्धार कीजिये और है कमलूनयन ! हमको झान्ति प्रदान कोजिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.378)
- **Original**: आपके द्वारा यह सर्गकी प्रवृत्ति संसारका उपकार करनेवाल्ली हो। हे कमलनयन ! आपको नमस्कार है, आप हमको शान्ति प्रदान कोजिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.379)
- **Original**: श्रीपराशरजी बोले--इस प्रकार स्तुति किये जानेपर पुृथिवौकों धारण करनेजाले परमात्मा वराहजीने उसे शीघ्र ही उठाका अपार जलके ऊपर स्थापित कर दिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.380)
- **Original**: उस जलसमूहके ऊपर बह एक बहुत बड़ो नौकाके समान स्थित है और बहुत विस्तृत आकार होनेके कारण उसमें डुबती नहीं है
- **Translation**: 

---

