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

### Verse 1 (Vishnu Puran 0.1621)
- **Original**: 83 न सस्यानि न गोरक्ष्य न कृषिन वणिकृपथ: । वैन्यात्मभृति मैत्रेय सर्वस्यैतस्य सम्मवः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1622)
- **Original**: 84 अश्य अंश 577 अपने पीछे आते देखा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1623)
- **Original**: तब उन प्रबक् पराक्रमी महाराज पृथुसे, उनके वाणफ्रहारसें बचनेकी कामनासे काँपती हुई पृथिवों इस प्रकार बोली
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1624)
- **Original**: पृथिवीने कहा--हे राजेद्ध ! बया आपको ख्यो- वधका महापाप नहीं दीख पड़ता, जो मुझे मारनेपर आप ऐसे उतारू हो रहे हैं 2
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1625)
- **Original**: पृथ्ु बोल्के--जहाँ एक अनर्थकारीको मार देनेसे बहूतोंको सुख्त्र प्राप्त हो उसे मार देना ही पुषण्यप्रद है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1626)
- **Original**: पृथिवी खोली--हे नृपश्रेष्ट ! यदि आप प्रजाके हितके लिये ही मुझे मारना चाहते हैं तो [ पेंरे पर जानेपर ] आपकी प्रजाका आधार क्या होगा ?
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1627)
- **Original**: पृथुने कहा--अरी वसुधे ! अपनी आज्ञाका उल्लड्जुन करनेवाल्मी तुझे मारकर मैं अपने योगबलसे ही इस प्रजाको धारण करूँगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1628)
- **Original**: श्रीपराशरजी कोले--तब अत्पत्त भयभीत एवं क्यॉपती हुई पृथिवीने उन पृथिवीपतिको पुनः प्रणाम करके कहा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1629)
- **Original**: पृथिलरी खोल्ली--हे राजन्‌ ! यल्पूर्वक आरम्भ किये हुए सभी कार्य सिद्ध हों जाते हैं । अतः मैं भी आपको एक उपाय बताती हूँ; यदि आपकी इच्छा हो तो वैसा ही करें
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1630)
- **Original**: हे नस्नाथ ! मैंने जिन समस्त ओषघधियोंको पत्ना रतिया है उन्हें यदि आपकी इच्छा हो तो दुग्धरूपसे मैं दे सकती हूँ।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1631)
- **Original**: अतः. है धर्मात्माओमें श्रेष्ठ महाराज ! आप प्रजाके हितके लिये कोई ऐसा वत्स (बछड़ा) बनाइये जिससे वात्सल्यवश मैं उन्हें दुग्धरूपसे निकाल सकूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1632)
- **Original**: और मुझको आप सर्वत्र समतलऊ कर दीजिये जिससे मैं उत्तमोत्तम ओषधियोके चोजरूप दुष्घको सर्वत्र उत्पन्न कर सकूँ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1633)
- **Original**: श्रीपराधरजी बोले--तब महाराज पृथुने अपने धनुषकी क्व्रेटिसे सैकड़ों-हजाएों पर्वतोंकों उस्वाड़ा और उन्हें 'एक स्थानपर इकट्ठा कर दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1634)
- **Original**: इससे पूर्व पृथिवीफे समतरू न होनेसे पुर और प्राम आदिका कोई नियमित विभाग नहों था
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1635)
- **Original**: हे मैत्रेय ! उस समय अन्न, गोरक्षा, कृषि और व्यापारका भो कोई क्रम न था
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1636)
- **Original**: यह सत्र तो चेनपुत्र पृथुके समयरों ही आरम्भ हुआ है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1637)
- **Original**: 8 आआआआ ्रीविध्णपुराण _ #आ#आ#आ##आ#आ 93 श्रीविष्णुपुराण [ आ* 13 य्रन्न यत्र सम॑ त्वस्या भूमेरासीदब्विजोत्तम । तत्न तत्र प्रजा: सर्बा निवार्स समरोच्नयन्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1638)
- **Original**: 85 आहार: फलपूलानि प्रजानामभवत्तदा । कृच्छेण महता सो5पि प्रणष्टास्वोषधीषु लै ।। 86 स कल्पयित्वा व्सं तु मनु स्वायम्भुवं प्रभुम स्वपाणों पृथ्चिवीनाथो दुदोह पृथित्रीं पृथुः । सस्यजातानि सर्वाणि प्रजानां हितकाम्यया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1639)
- **Original**: 87 तेनान्नेन प्रजास्तात वर्तन्तेद्यापि नित्यशः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1640)
- **Original**: <8 तत्तत्पात्रमुपादाय तत्तददुग्ध॑मुने वत्सदोग्धृविशेषाश्ष तेषां तद्योनयो3भवन्‌
- **Translation**: 

---

