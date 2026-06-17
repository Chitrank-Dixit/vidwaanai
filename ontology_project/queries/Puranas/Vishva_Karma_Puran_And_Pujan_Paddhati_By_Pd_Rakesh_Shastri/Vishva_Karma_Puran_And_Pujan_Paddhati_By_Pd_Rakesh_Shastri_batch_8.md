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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.141)
- **Original**: दीपक-सूतवास-समायुक्तें. कर्पूरादि-समन्वितमू । दीप गृहाण देवेश ! ह्न्धकार-विनाशनमू
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.142)
- **Original**: नैकेदय- पूष-मोदक-संयाव-पयः पक्‍्वादिकं वरमू । निर्मित॑ बहुसत्कारैनैंवियं_ प्रतिगूह्ाताम्‌
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.143)
- **Original**: औआचमन-शीतल्ं स्वादुः गांगेयं॑ तृषा-तृप्तिकरं जलमू । सर्वदैव म्वतृप्त्यर्थ विश्वकर्मन्‌ ! प्रगृह्ातामू
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.144)
- **Original**: स्व घधिरसो पेत॑ पवित्र सरिता-जलम्‌ । आचम्य॑ च मया दत्त गृहाण देवताप्रिय
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.145)
- **Original**: फल-इदें फल मया देव ! स्थापित्तं पुरतस्तद । तेन मे सफलादाप्तिवेज्जन्मनि जन्मनि
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.146)
- **Original**: ताम्बूल-ताम्बूल॑ पूंगसंयुक्ते चूर्ण खादिर्संयुतमू। लवेंगादियुतं देव ! गृह्मतां ब्रह्म-वंशज
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.147)
- **Original**: दक्षिणा--हिरण्कार्भ-गर्भस्थ.. हेमबीजं. विभावसोः। अनन्तपुण्यफलदमतः शान्ति प्रयच्छ मे
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.148)
- **Original**: एवं विधिवत्‌ विश्वकर्मा जी के पूजन के पश्चात्‌ यन्त्र, निहाय एवं विविध प्रकार के औजारों की पूजा करके अग्नि-स्थापन के साथ विधिवत्‌ हवन यज्ञ करे । तत्पश्वात्‌ आचार्यादि विद्वान ब्राह्मणों को भोजन कराकर यथा शक्ति दान, दक्षिणा देवे । अन्त में विश्वकर्मा भगवान की आरती करके देवताओं का विसर्जन करे तथा प्रसाद वितरण करे । हवन मन्त्र विसर्जन करने से पहले अग्नि का विधिवत्‌ पूजन करके निम्नलिखित मन्त्र से घृत द्वारा हवन करे। ऊँ प्रजापतये स्वाहा, इदं॑ प्रजापतये न मम । ऊँ इन्द्राय स्वाहा, इद॑ इन्द्राय न मम। ऊँ अग्नये स्वाहा, इदमग्नये न सम। ऊँ सोसाय स्वाहा, इदं सोमाय न मम। ऊँ भू: स्वाहा, इदमग्नये . न मम। ऊँ भवः स्वाहा, इदं॑ वायवे न मम। श्री विश्वकर्पा पुराण एवं पूजन पद्धति 9
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.149)
- **Original**: ऊँ स्वः स्वाहा, इदं॑ सूयाय न मम। एता: सप्त महाव्याइतयः (घृताहुतिश । इसके बाद खीर या शाकत्य द्रव्य से मूल मन्त्र द्वारा कम से कम एक माला हवन करे । ः ' मूल मन्त्र यथा-(108 बार . ऊँ विश्वकर्मणे नमः स्वाहा । उसके बाद नवग्रह, इष्टदेव आदि का हवन इस प्रकार करे। ऊँ सूर्याय नमः स्वाहा, चन्द्रमसे नमः स्वाहा, भौमाय नमः स्वाहा, बुधाय नमः स्वाहा, गुरवे नमः स्वाहा, शुक्राय नमः स्वाहा, शनैश्चवराय नमः स्वाहा, राहवे नमः स्वाहा, केतवे नमः स्वाहा, पश्नलोकपालेग्यो नमः स्वाहा, दशदिक्पालेम्यो नमः स्वाहा, इष्टदेवेभ्यो नमः स्वाहा, कुलदेवेग्यो नमः स्वाहा, ग्रामदेवेग्यो नमः स्वाहा, सर्वेभ्यो देवेग्यो नमः स्वाहा, सर्वाभ्यो देवीभ्यो नमः स्वाहा । पूर्णहुति-रँ» मूघानिं दिवो अरतिं पृथिव्या वैश्वानरुपृत अजातमस्निमू । कवि सप्राजमतिर्थि जनानामासन्ना पात्र जनयन्त देवा: स्वाहा । भस्म-ऊेँ: च्यायुषमू जमदग्ने:-इति ललाटे, कश्यपस्य च्यायुषमू इति ग्रीवायाम्‌ । यद्देवेषु च्यायुषमू-इति दक्षिणबाहुमूले । तज्नोउअस्तु च्यायुषम्‌-इति हदये । इसके बाद होता, पुरोहित एवं आचार्य को दक्षिणा देकर विसर्जन करे । पी कर्पूरवर्तिसंयुक्त गोघृतेन सुपूरितम्‌ । नीराज़न॑... गृहाणेद॑ कृपया सौख्यवर्द्धन !
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.150)
- **Original**: नानासुगन्धिपुष्पाणि यथाकालोद्धवानि च। पुष्पाज्लिस्वरूपणि .. गृद्मातां.. वास्तुनन्दन !
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.151)
- **Original**: प्रदक्षिणा-यानि कानि च पापानि जन्मान्तरकृतानि च। . तानि सवाणि नश्यन्तु प्रदक्षिण पढदे-पदे
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.152)
- **Original**: अन्त में इस मन्त्र से विसर्जन करे- समस्तैरुपचारैश्न याउअर्चनाइ्त्र मया. कृता। सा सर्वा पूर्णतां यातु हापराधं क्षमस्व मे
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.153)
- **Original**: आवाहनं न जानामि न जानामि विसर्जनमू। पूजां चैव न जानामि तव ग़तिर्दीनवत्सल !
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.154)
- **Original**: देवशिल्पिनन्‍्महाभाग !.. देवानां... कार्यसाघक। विश्वकर्मनू नमस्तुभ्यं सदा शान्ति प्रयच्छ मे
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.155)
- **Original**: यान्तु देवगणा: सर्वे पूजामादाय मामकीमू। कामनाउमीष्ट-सिद्धचर्थ. पुनरागमनाय च
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.156)
- **Original**: इति विश्वकर्मा पूजन पद्धतिः समाप्त
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.157)
- **Original**: [20 श्री विश्वकर्मा पुराण एवं पूजन पद्धति] श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.158)
- **Original**: विश्वकर्मा कवच श्रीमत्परात्पर विश्वकर्मपर ब्रह्मणेनम:
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.159)
- **Original**: अथ श्री विश्वकर्मा कवच प्रारम्म:
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.160)
- **Original**: अस्य श्री विश्वकर्म परव्रह्म कवचस्तोत्न चतुर्विशत्य क्षरमूलमहामंत्रस्यानुग्रहार्थ परब्रह्रऋषि:
- **Translation**: 

---

