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

### Verse 1 (Vishnu Puran 0.1821)
- **Original**: ऋषि खोल्के---अयि भीरु ! यह तू ठीक कहती है, या हे झुभे ! मेरी हँसी करतो है ? मुझे तो ऐसा ही प्रतीत होता है कि मैं इस स्थानपर तेरे साथ केवल एक ही दिन दिनपेकमहं मन्ये त्वया सार्द्धमेहासितम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1822)
- **Original**: रहा हूँ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1823)
- **Original**: # दश्शिणा नायिकाका लक्षण इस प्रकार कहा है-- था गौर भरत प्रेम सद्धाव॑ पूर्वतायके। न सुशत्यन्यसक्तापि सा ज्लेया दक्षिणा युधै;
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1824)
- **Original**: अन्य नायकमें आसक्त रहते हुए भी जो अपने पूर्व-नायककों गौरक भय, प्रेम और सद्भावके क्रारण न छोड़ती हो उसे 'दक्षिणा' जानन्य चाहिये। दक्षिणाके गुणकों 'दाक्षिण्य' कहते हैं ।
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1825)
- **Original**: आत्95 ] प्रम्त्म्नेचोचाच वदिष्याम्यनृ्त ब्रह्मन्कथमत्र तवान्तिके । विशेषेणाद्य भवता पृष्टा मार्गानुवर्तिना
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1826)
- **Original**: 34 सोम उवाच निदहाम्य तद्लः सत्यं स सुनिर्नुपननन्‍्दना: । धिगधिड मामित्यतीबेत्थं निनिन्‍्दात्मानमात्मना
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1827)
- **Original**: मुन्ल्किच तपांसि मम नष्टानि हते ब्रह्मलिदां धनम्‌। हतो विवेक: केनापि योषित्मोहाय निर्धिता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1828)
- **Original**: 36 ऊर्मिषटकातिगं ब्रह्म ज्ञेयमात्मजयेन में। प्रतिरेषा हता येन थधिक्‌ ते काम महाग्रहम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1829)
- **Original**: 37 ब्रतानि वेदलेधाप्तिकारणान्यखिलानि च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1830)
- **Original**: नरकप्राममार्गेण सड्लेनापहतानि मे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1831)
- **Original**: 38 गर्छ पापे यथाकामं यत्कार्य तत्कृतं त्वया । देवराजस्य मत्क्षोभं कुर्वन्त्या भावचेष्टिति:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1832)
- **Original**: 40 न त्वां करोम्यहं भस्म क्रोधतीव्रेण वह्निना । सतां सप्तपद मैत्रमुषितोडह॑ त्ववा सह
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1833)
- **Original**: 41 अथवा तब को दोष: किं वा कुप्याम्यहं तव । ममैव दोषों नितरां येनाहमजितेन्द्रिय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1834)
- **Original**: 42 यया दाक्कप्रियार्थिन्या कृतो मे तपसो व्यय: । त्वया भिक्तां महामोहमझ्जूषां सुजुगुप्सिताम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1835)
- **Original**: 43 सोम उषाच यावदिल्थ॑ स विप्रर्षिस्तों ब्रवीति सुमध्यमाम्‌ । तावडलत्खेदजला सा बभूवातिवेपथु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1836)
- **Original**: डड प्रवेषमानां सतत स्विन्नगात्रलूता सतीम्‌। गच्छ गच्छेति सक्रोधमुवाच मुनिसत्तम:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1837)
- **Original**: 45 सातुनिर्भत्सिता तेन विनिष्क्रम्य तदाश्रमात्‌ । आकाशगामिनी स्वेद॑ ममार्ज तरुपललबैः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1838)
- **Original**: 46 5 अम्लोचा खोली--हे ब्रह्मम्‌ ! आपके निकट मैं झूठ कैसे बोल सकती हूँ ? और फिर विशेषतया उस समय जब कि आज आप अपने धर्म-मार्गका अनुसरण कऋलनेमें तत्पर होकर मुझसे पूछ रहे है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1839)
- **Original**: सोमने कहा--हे राजकुमाये ! उसके ये सत्य बचन सुनकर मुनिने 'मुझे घिकार है ! मुझे धिकार है !' ऐसा कहकर स्वयं ही अपनेको बहुत कुछ भल्म- खुरा कहा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1840)
- **Original**: सुनि खोसे--ओह ! मेरा तप नष्ट हो गया, जो ब्रह्मवेत्ताओंका घन था वह लुुट गया और वियेकबुद्धि मारी गयी ! अहो
- **Translation**: 

---

