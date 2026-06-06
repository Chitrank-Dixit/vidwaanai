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

### Verse 1 (Bhagwat_Geeta 10.919)
- **Original**: विस्तरेणात्मनो योगं विभूतिं च जनार्दन। भूय: कथय तृप्तिहिं श्रुण्वतो नास्ति मेउमृतम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 10.920)
- **Original**: हे जनार्दन! अपनी योगशक्तिको और विभूतिको फिर भी विस्तारपूर्वक कहिये, क्योंकि आपके अमृतमय वचनोंको सुनते हुए मेरी तृप्ति नहीं होती अर्थात्‌ सुननेकी उत्कण्ठा बनी ही रहती है
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 10.921)
- **Original**: 134 * श्रीमद्धगवद्रीता * श्रीभयवानुवाच हन्त ते कथयिष्यामि दिव्या ह्यात्मविभूतय: । प्राधान्यत: कुरु श्रेष्ठ नास्त्यन्तो विस्तरस्य मे
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 10.922)
- **Original**: श्रीभगवान्‌ बोले--हे कुरुश्रेष्ठ ! अब मैं जो मेरी दिव्य विभूतियाँ हैं, उनको तेरे लिये प्रधानतासे कहूँगा; क्योंकि मेरे विस्तारका अन्त नहीं है
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 10.923)
- **Original**: अहमात्मा गुडाकेश सर्वभूताशयस्थित:। अहमादिश्व मध्यं च भूतानामन्त एव च
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 10.924)
- **Original**: हे अर्जुन! मैं सब भूतोंके हृदयमें स्थित सबका आत्मा हूँ तथा सम्पूर्ण भूतोंका आदि, मध्य और अन्त भी मैं ही हूँ
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 10.925)
- **Original**: आदित्यानामहं विष्णुर्ज्योतिषां रविरंशुमान्‌। मरीचिर्मरुतामस्मि नक्षत्राणामह॑ शशी
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 10.926)
- **Original**: मैं अदितिके बारह पुत्रोंमें विष्णु और ज्योतियोंमें किरणोंवाला सूर्य हूँ तथा मैं उनचास वायुदेवताओंका तेज और नक्षत्रोंका अधिपति चन्द्रमा हूँ
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 10.927)
- **Original**: वेदानां सामवेदो5स्मि देवानामस्मि वासव: । इन्द्रियाणां मनश्रास्मि भूतानामस्मि चेतना
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 10.928)
- **Original**: । मैं वेदोंमें सामवेद हूँ, देवोंमें इन्द्र हूँ, इन्द्रियोंमें मन हूँ और भूतप्राणियोंकी चेतना अर्थात्‌ जीवनशक्ति हूँ
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 10.929)
- **Original**: * अध्याय 10* 135 रुद्राणां शट्भूरश्चास्मि वित्तेशो यक्षरक्षसाम्‌। वसूनां पावकश्चास्मि मेर: शिखरिणामहम्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 10.930)
- **Original**: मैं एकादश रुद्रोंमें शंकर हूँ और यक्ष तथा राक्षसोंमें धनका स्वामी कुबेर हूँ। मैं आठ वसुओंमें अग्नि हूँ और शिखरवाले पर्वतोंमें सुमेरु पर्वत हूँ
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 10.931)
- **Original**: पुरोधसां च मुख्य मां विद्द्वि पार्थ बृहस्पतिम्‌ । सेनानीनामहं स्कन्दः सरसामस्मि सागरः
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 10.932)
- **Original**: पुरोहितोंमें मुखिया बृहस्पति मुझको जान। हे पार्थ ! मैं सेनापतियोंमें स्कन्‍्द और जलाशयोंमें समुद्र हूँ
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 10.933)
- **Original**: महर्षीणां भूगुरहं॑ गिरामस्म्येकमश्षरम्‌ । यज्ञानां जपयज्ञो5स्मि स्थावराणां हिमालय:
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 10.934)
- **Original**: मैं महर्षियोंमें भुगु और शब्दोंमें एक अक्षर अर्थात्‌ ओंकार हूँ। सब प्रकारके यज्ञोंमें जपयज्ञ और स्थिर रहनेवालोंमें हिमालय पहाड़ हूँ
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 10.935)
- **Original**: अश्वत्थ: सर्ववृक्षाणां देवर्षीणां चर नारद: । गन्धर्वाणां चित्ररथ: सिद्धानां कपिलो मुनि:
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 10.936)
- **Original**: मैं सब वृक्षोंमें पीपलका वृक्ष, देवर्षियोंमें नारद मुनि, गन्धर्वोर्में चित्ररथ और सिद्धोंमें कपिल मुनि हूँ
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 10.937)
- **Original**: उच्चै: भ्रवसमश्चानां विद्द्धि माममृतोद्धवम्‌। ऐरावतं गजेन्द्राणां नराणां च नराधिपम्‌
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 10.938)
- **Original**: 136 * श्रीमद्धगवद्रीता * घोड़ोंमें अमृतके साथ उत्पन्न होनेवाला उच्चै: श्रवा नामक घोड़ा, श्रेष्ठ हाथियोंमें ऐरावत नामक हाथी और मनुष्योंमें राजा मुझको जान
- **Translation**: 

---

