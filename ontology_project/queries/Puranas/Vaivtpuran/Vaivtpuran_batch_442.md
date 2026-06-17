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

### Verse 1 (Vaivtpuran 23.1802)
- **Original**: पुण्यमय नारायणाश्रमको चले गये। उनकी पत्नी हैं। (अध्याय 28) >ज2>2जमलपीए॑ए9/0 700 बदरिकाश्रममें नारायणके प्रति नारदजीका प्रश्न सौति कहते हैं--शौनक! देवर्षि नारदने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1803)
- **Original**: उन्होंने रमणीय रज्ञमय सिंहासनपर बिठाया। उस नारायण ऋषिके आश्चर्यमय आश्रमकों देखा, जो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1804)
- **Original**: रमणीय आसनपर बैठकर नारदजीने रास्तेकी बेरके बनोंसे सुशोभित था। नाना प्रकारके वृक्षों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1805)
- **Original**: थकावट दूर की और उन ऋषिश्रेष्ठ सनातन और फलोंसे भरे हुए उस आश्रममें कोयलकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1806)
- **Original**: भगवान्‌ नारायणसे, साथ ही उन सब परम दुर्लभ मीठी कूक मुखरित हो रही थी। बड़े-बड़े शरभों,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1807)
- **Original**: मुनियोंसे भी पूछा, जो पिताके स्थानमें वेदाध्ययन सिंहों और व्याप्रसमुदायोंसे घिरे होनेपर भी उस करके वहाँ विराजमान थे। आश्रममें ऋषिराज नारायणके प्रभावसे हिंसा और। नारदजी खोले--प्रभो! योगीश्वर शंकरसे भयका कहीं नाम नहीं था। वह विशाल वन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1808)
- **Original**: ज्ञान और मन्त्रका उपदेश पाकर भी मेरा मन जनसाधारणके लिये अगम्य और स्वर्गसे भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1809)
- **Original**: तृत्त नहीं हो रहा है; क्योंकि यह बड़ा चञ्चल अधिक मनोहर था। वहाँ नारदजीने देखा--ऋषिप्रवर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1810)
- **Original**: है और इसे रोकना अत्यन्त कठिन है। मेरे मनमें नारायण मुनियोंकी सभामें रत्ममय सिंहासनपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1811)
- **Original**: प्रधुकी कुछ ऐसी प्रेरणा हुई, जिससे मैंने आपके विराजमान हैं। उनका रूप बड़ा मनोहर है और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1812)
- **Original**: चरणारविन्दोंका दर्शन किया। इस समय मेँ वे योगियोंके गुरु हैं। श्रीकृष्णस्वरूप परमेश्वर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1813)
- **Original**: आपसे कुछ विशेष ऐसा ज्ञान प्राप्त करना चाहता परब्रह्मका जप करते हुए नारायण मुनिका दर्शन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1814)
- **Original**: हूँ, जिसमें श्रीकृष्णके गुणोंका वर्णन हो, जो कि करके ब्रह्मपुत्र नारदने उन्हें प्रणाम किया। उन्हें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1815)
- **Original**: जन्म, मृत्यु और जराका नाश करनेवाला है। आया देख नारायणने सहसा उठकर हृदयसे लगा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1816)
- **Original**: भगवन्‌! ब्रह्मा, विष्णु और शिव आदि देवता, लिया और उत्तम आशीर्वाद प्रदान किया। साथ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1817)
- **Original**: देवराज इन्द्र, मुनि और विद्वान्‌ मनु किसका ही स्लेहपूर्वक्क कुशल-समाचार पूछा और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1818)
- **Original**: चिन्तन करते हैं? सृष्टिका प्रादुर्भाव किससे होता आतिथ्यसत्कार किया। फिर नारदजीकों भी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1819)
- **Original**: है अथवा उसका लय कहाँ होता है? समस्त
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1820)
- **Original**: कारणोंके भी कारणभूत सर्वेश्वर विष्णु कौन हैं? . नारदजीका यह वचन सुनकर भगवान्‌ जगत्पते! उन ईश्वरका रूप अथवा कर्म क्‍या है ? नारायण ऋषि हँसे। फिर उन्होंने त्रिभुवनपावनी इन सब बातोंपर मन-हो-मन विचार करके आप
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1821)
- **Original**: पुण्यकथाको कहना आरम्भ किया। बतानेकी कृपा करें। (अध्याय 29) ढअलज0 मय 400000000 नारायणके द्वारा परमपुरुष परमात्मा श्रीकृष्ण तथा प्रकृतिदेवीकी महिमाका प्रतिपादन श्रीनारायण बोले--गणेश, विष्णु, शिव,
- **Translation**: 

---

