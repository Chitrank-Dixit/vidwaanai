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

### Verse 1 (Vishnu Puran 0.7921)
- **Original**: तदिद॑ स्थमन्तकरलं गृह्मतामिच्छया यस्थाभिमतं तस्य समर्प्यताम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7922)
- **Original**: ततः स्वोदरबख्ननिगोपितमतिछघुकनक- समुहझकगतं प्रकटीकृतवान्‌ू
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7923)
- **Original**: ततश्व निष्क्राम्य स्थमनतकम्णिं तस्मिन्यदुकुलसमाजे मुमोच्च
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7924)
- **Original**: मुक्तमात्रे चर तस्मिन्नति- चतुर्थ अंडा 279 निरन्तर अखण्ड यज्ञानुष्टान करता रहता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7925)
- **Original**: और इसके पास यक्ञके साधन [धन आदि] भी बहुत कम हैं; इसलिये इसमें सनदेह् नहीं कि इसके पास स्थमन्तकमणि अवश्य है।' ऐसा निश्चयकर किसी और प्रयोजनके उद्देइयसे उन्होंने सम्पूर्ण यादपॉंको अपने महलमें एकत्रित किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7926)
- **Original**: समस्त यदुवंशियोकि वहाँ आकर बैठ जानेके बाद प्रथम प्रयोजन बताकर उसका उपसंडहार होनेपर प्रसज्ञातनरसे अक्रूरके साथ परिहास करते हुए भगवान्‌ कृष्णने उनसे कहा--
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7927)
- **Original**: “हे दानपते ! जिस प्रकार शतधन्वाने तुम्हें सम्पूर्ण संसारकी सारभूत यह स्थमन्‍तक नामक महामणि सौंपी थी वह हमें सत्र मालूम है । बह सप्पूर्ण राष्टरका उपकार करती हुई तुम्हारे पास है तो रहे, उसके प्रभावका फल तो हम सभी भोगते हैं, किन्तु ये बलभद्रजी हमारे ऊपर सन्‍्देह करते थे, इसलिये हमारी प्रसन्नताके लिये आप एक बार उसे दिखला दीजिये।'” भगवान्‌ वासुदेवके ऐसा कहकर चुप हो जानेपर रत्न साथ ही लिये रहनेके कारण अक्रूरजी सोचने लंगे--
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7928)
- **Original**: “अब मुझे क्या करना चाहिये, यदि और किसी प्रकार कहता हूँ तो केषछ खस्बॉकि ओटमें स्टोलनेपर ये उसे देख ही लेंगे और इनसे अत्यन्त विरोध करनेमें हमारा कुशल नहीं है।'' ऐसा सोचकर निखिल संसारके कारणस्वरूप श्रीनारायणसे अक्वूरजी बोले--
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7929)
- **Original**: “भगवन्‌ ! झतघन्वाने मुझे वह मणि सौंप दी थी। उसके मर जानेपर मैंने यह सोचते हुए बड़ी ही कठिनतासे इसे इतने दिन अपने पास रखा है कि भगवान्‌ आज, कहलू या परसों इसे माँगेंगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7930)
- **Original**: इसकी चौकसीके क्लेडसे सम्पूर्ण भोगॉमें अनासक्तचित्त होनेके ऋारण मुझे सुखक्ता लेझामात्र भो नहीं मिल्त्र
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7931)
- **Original**: भगवान्‌ ये बिचार करते कि, यह सम्पूर्ण राष्ट्रके उपकास्क इतने-से भारकों भी नहीं उठा सकता, इसलिये स्वयं मैंने आपसे कहा नहीं।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7932)
- **Original**: ऊग, कीजिये आपयत्र वह स्पमन्तकमणि यह रहो, आपकी जिसे इच्छा हो उसे ही इसे डे दीजिये”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7933)
- **Original**: तब अक्रूरजीने अपने कटि-वस्नरमें छिपाई हुई एक छोटी-सी सोनेकी पिटारीमें स्थित वह स्थमन्‍्तकमणि प्रकट की और उस पिटारीसे निकालकर यादवसमाजमें रख दी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7934)
- **Original**: 147-146
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7935)
- **Original**: डसके रखते ही यह सम्पूर्ण स्थान कान्या तदखिलमास्थानमुदयोतितम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7936)
- **Original**: उसकी तीत्र कान्तिसे देदीप्यमान होने लगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7937)
- **Original**: 280 श्रीविष्णुपुराण [ अ* 13 अथाहाक़ूर: स एप मणि: शतथ्नन्बनास्माक समर्पितः यस्याय॑ स एन॑ गृद्वातु डृति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7938)
- **Original**: तमालोक्य सर्वयादवानां साधुसाध्विति विस्मितमनसां वाचोउश्रूयत्त
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7939)
- **Original**: तमास्मेक्यातीव बलभद्रो. ममायमच्युतेनैव सामान्यस्समन्यीप्सित इति कृतस्पृहो5भूत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7940)
- **Original**: ममैवायं पितृथनमित्यतीव च सत्यभामापि स्पृहयाक्षकार
- **Translation**: 

---

