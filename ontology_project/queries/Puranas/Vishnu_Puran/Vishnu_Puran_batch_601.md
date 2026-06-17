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

### Verse 1 (Vishnu Puran 0.12001)
- **Original**: सत्ययुग, त्रेता, द्वाप' और कक्ति--ये चार युग हैं, इन सबका काल मिल्माकर बारह हजार दिव्य वर्ष कहा जाता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12002)
- **Original**: है मैत्रेय ! [प्रत्येक्र सन्‍्वन्तरके] आदि कृतयुग और अन्तिम कलियुगको छोड़कर शोष सब चतुर्युग स्वरूपसे एक समान हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12003)
- **Original**: जिस प्रकार आइय (प्रथम) सत्ययुगमें ब्रह्माजी जगत्‌की रचना करते हैं उसी प्रकार अन्तिम कलियुगमें वे उसका उपसंहार करते हैं।। 7
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12004)
- **Original**: शमैश्रेयजी खोले--हे भगवन्‌ ! कलिके स्वरूपका विस्तारसे वर्णन कीजिये, जिसमें चार चरणोंवाले भगवान्‌ धर्मका प्रायः ल्त्रेप हो जाता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12005)
- **Original**: ओऔपराशरजी बोले--हे मैत्रेय! आप जो कलियुगका स्वरूप सुनना चाहते हैं सो उस समय जो कुछ होता है बह संक्षेपसे सुनिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12006)
- **Original**: कल्लियुगमें मनुष्योंकी प्रवृत्ति वर्णाश्रम-धर्मानुकूल नहीं रहती और न बह ऋकू-साम-यजुरूप त्रयी-धर्मका सम्पादन करनेवाली हो होतो है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12007)
- **Original**: उस समय धर्मक्वाह, गुरु-दिष्य- सम्बन्धकी स्थिति, दाम्पत्यक्रम और अग्निमें देवयकञ- क्रियाका क्रम (अनुष्ठान) भी नहीं रहता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12008)
- **Original**: डरेड रेड :&:&+
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12009)
- **Original**: स्‍अखत्रीविष्णुपराण (1 [ आ* 1 यत्र कुत्र कुले जातो बली सर्वेश्वरः कलौ । कलियुगमें जो बलवान्‌ होगा वही सबका स्वामी होगा सर्वेभ्य एव बर्णेश्यो योग्य: कन्यावरोधने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12010)
- **Original**: चाहे किसी भी कुलमें क्यों न उत्पन्न हुआ हो, वह सभी येन केन च योगेन द्विजातिदीक्षित: कलो । यैब सैव च मैत्रेय प्रायश्चित्त कल्लो क्रिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12011)
- **Original**: 13 सर्वमेव कल्मे शास्त्र यस्थ यद्वचनं द्विज । देवता च कलौ सर्वा सर्वस्सर्वस्थ चाश्रम:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12012)
- **Original**: 14 उपवासस्तथायासो वित्तोत्सर्गस्तप: कलौ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12013)
- **Original**: धर्मो यथाभिरुचितैरनुष्ठानैरनुष्ठितः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12014)
- **Original**: 15 वित्तेन भविता पुंसां स्वल्पेनाब्यमद: कलौ । ख्रीणां रूपमदश्लैत॑ केशैरेव भविष्यति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12015)
- **Original**: 16 सुवर्णमणिरत्रादों वस्त्रे चोपक्षयं गते। कलौ ख्तरियो भविष्यन्ति तदा केशैरलडकृता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12016)
- **Original**: 17 परित्यक्ष्यन्ति भर्त्तारें वित्तहीनं तथा खरिय: । भर्त्ता भविष्यति कलौ वित्तवानेव योषिताम्‌ ।। 18 यो वै ददाति बहुल स्व॑ स स्वामी सदा नृणाम्‌ । स्वामित्वहेतुस्सम्बन्धो न चाभिजनता तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12017)
- **Original**: 19 गृहान्ता द्रव्यसज्ञाता द्रव्यान्ता च तथा मति: । अर्थाश्षात्मोपभोम्यान्ता भविष्यन्ति कल्लौ युगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12018)
- **Original**: 20 ख्रियः कलौ भविष्यन्ति स्वैरिण्यो लल्ितिस्पृहा: । अन्याबावाप्ततित्तेषु पुरुषा: स्पृहयालव:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12019)
- **Original**: 29 अभ्यर्थितापि सुहददा स्वार्थहानिं न मानवा: । पणार्धारधार्द्धमात्रेषपि करिष्यन्ति कल्ौ द्विज
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12020)
- **Original**: 22 समानपौरुष चेतो भावि विप्रेषु ले कल्मौ । क्षीरप्रदानसम्बन्धि भावि गोषु चर गौरबम्‌
- **Translation**: 

---

