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

### Verse 1 (Markende Puran 0.621)
- **Original**: सूर्योटण न होनेके कारण बराबर रात हो रहते हो रहा था। केवल बिजलीके चमकनेसे पार्ग' लगी। कितने ही दिनोंके बराजर सपय रातभस्में दिखाबी दे जाता था। ऐसी ज्ेलामें बह न्राह्मणी
- **Translation**: 

---

### Verse 2 (Markende Puran 0.622)
- **Original**: ही बीत गया। हससे देवताओंकों बड़ा भय हुआ। अपने पतिय7 अभोष्ट साधन करनेके लिये गजपार्गसे वे सोचने लगे-स्वाध्वाय, बषटआ, स्वका ( ध्राद्ध) जो रहा थी। मार्गपें सूलौं थो, जिसके ऊपर चोर
- **Translation**: 

---

### Verse 3 (Markende Puran 0.623)
- **Original**: तथा स्वाहा (यज्ञ)-से रहित होकर ग्रह सार ने होते हुए, भी चोरके सन्देहसे माण्डब्य नापक जगत नए हुए बिना कैसे रह सकता हैं। द्विन भ्राह्मणको चढ्गा दिवा दया था। ते दु:ख आतुर
- **Translation**: 

---

### Verse 4 (Markende Puran 0.624)
- **Original**: ग़तक्ी व्यवस्था हुए बिना मास और ऋतुका भी हो रहे थे। कौशिक पत्ञोंके कंग्रेपर बैठा था, उस, लोप हो जायगा। उनके लोप होनेसे दक्षिणायन अन्धकारमें देख न सकनेके कारण उसने अपने
- **Translation**: 

---

### Verse 5 (Markende Puran 0.625)
- **Original**: और उत्तरायणका भी ज्ञान नहीं होगा। अयनक्ा चैरोंसे छूकर मूलोकों हिला दिया। इससे कुपित
- **Translation**: 

---

### Verse 6 (Markende Puran 0.626)
- **Original**: ज्ञान हुए बिना वर्ष कैसे हो भरता हैं, और क्षर्पके हॉकर माण्डड्यने कहा-“जिसने पैरसे हिलाकर
- **Translation**: 

---

### Verse 7 (Markende Puran 0.627)
- **Original**: बिना कालका झ्त्र होता असम्भव हैं। पतिव्रताके मुझे इस कष्टमी दशार्में पहुँचा दिया और पुझ्े । वचनसे सूर्यका उदय हीं नहीं होता; उसके ब्रिता अत्यन्त दुखी कर दिया, श्रह गापात्मा नराथम स्नान, दान आर्टि क्रियाएँ अंद हो गयीं। अरस्नि- सूर्वोदय होनेपर व्बिश् हो तिसत्सन्देश अपने
- **Translation**: 

---

### Verse 8 (Markende Puran 0.628)
- **Original**: होज़ और बह्का अभाव भी दुृष्टिगोचर होने लगा 5 है। होमके बिना हमलोगोंकी ताए नहीं होतो!
- **Translation**: 

---

### Verse 9 (Markende Puran 0.629)
- **Original**: जब पनुष्य यज्ञकां यथोचित भाग देंक/ हमें तृप् करते हैं, तथ हम खेतोकों उपजके लिये त्र्पा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.630)
- **Original**: कश्के मनुष्योंपर अनुग्रह करते हैँ। नया अन्न चैल होनेपर भनुष्य फिर हमारे लिये यद्य करते हैं और
- **Translation**: 

---

### Verse 11 (Markende Puran 0.631)
- **Original**: टमलोग यज्ञादिद्वारा पूछित होनेपर उन्हें मनोवाए-छत भोग प्रदान करते हैं। हम नो भेत्मी ओर वर्षा ऋरते हैं और मनुष्य ऊपस्की ओर। हम जलकी बर्षसे मनुष्योंको और मनुष्य हविष्णकी चर्यासे हमलोगॉक्ो
- **Translation**: 

---

### Verse 12 (Markende Puran 0.632)
- **Original**: ठृप्त करते हैं । जो दुरात्या लोधन्नश हमारा यहा स्वयं खा लेते हैँ, उठ अपकारी पापियोंके नाशके
- **Translation**: 

---

### Verse 13 (Markende Puran 0.633)
- **Original**: लिये हम जल, सूर्य, आन, ज्राथु तथा पृश्न्नीको भी दृषित कर देते हैं। उन दूषित खस्तुऑका
- **Translation**: 

---

### Verse 14 (Markende Puran 0.634)
- **Original**: उपधोग करतेसे उठ कुकरमिंयोंक्रों नृत्युके लिये । भयड्डर महामारों आदि रौग उत्पन्न हो जाहे हैं। उन... >ममम»»»»कः.. आरा, +«म-ममममका कक 3 जनता ताजा. + +जभ्य धार्त्र तत: दुतल्ता तं सापमांतदारणम्‌ ! प्रोवाव व्यक्त सूर्खो नैयोदयपुएश्यात
- **Translation**: 

---

### Verse 15 (Markende Puran 0.635)
- **Original**: (16। 31)
- **Translation**: 

---

### Verse 16 (Markende Puran 0.636)
- **Original**: +दत्तात्रेबजोके जन्म प्रग्मक्ुमें पक पतित्नता ग्राह्मेणी तथा अनसूयाजीका चरित्र * 73 #&&5%2570 «»7
- **Translation**: 

---

### Verse 17 (Markende Puran 0.637)
- **Original**: 6:82:09 #ू&5 62255 ##4 5273 8:654 25:46 #74200%5:::52:0.07 64 65 2:7000074 646. 057 874 25444 जो हमें तृप्त करके शेष अन्न अपने उपभोगमें लाते
- **Translation**: 

---

### Verse 18 (Markende Puran 0.638)
- **Original**: अपने भ्र्मकों कुशल बतायी। हैँ, उन पह़ात्माओंकों हम पुण्यलोक प्रदान करते
- **Translation**: 

---

### Verse 19 (Markende Puran 0.639)
- **Original**: अनसूचा योलीं--कल्याणी! तुम अपने स्वापीके हैं। किन्तु इस समय प्रभातकाल हुए बिता इन
- **Translation**: 

---

### Verse 20 (Markende Puran 0.640)
- **Original**: मुखका दर्शन करके प्रसन्न तो रहती हो मनुष्योंके लिये वह सब पृण्यकर्म असम्भव हो
- **Translation**: 

---

